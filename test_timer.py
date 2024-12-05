import streamlit as st
import time
import threading
import os
from backend.prompt import PromptGenerator
from backend.groq_api_llm import GroqApi
from backend.deepgram_stt_tts import DeepgramAPI
from utils.audio import record_audio, play_audio


class VivaAutomationApp:
    def __init__(self):
        self.question_no = 1
        self.prompt_generator = PromptGenerator()
        self.groq_api = GroqApi()
        self.deepgram_api = DeepgramAPI()
        self.current_question = None
        self.current_answer = None
        self.evaluation_feedback = None
        self.total_score = 0
        self.max_questions = 2  # Changed to 5 questions
        self.sleep_duration = 1
        self.subject = "Machine Learning"  # Added subject name

    def generate_question(self):
        if self.question_no == 1:
            prompt = self.prompt_generator.generate_first_question_prompt()
        else:
            prompt = self.prompt_generator.generate_subsequent_question_prompt(
                self.current_question, self.current_answer, self.evaluation_feedback
            )
        self.current_question = self.groq_api.api_calls(prompt)

    def synthesize_and_play_question(self, question_text, output_file):
        self.deepgram_api.text_to_speech(
            text=question_text, output_file_path=output_file
        )
        play_audio(output_file)

    def record_answer(self, output_file):
        time.sleep(2)
        record_audio(file_path=output_file)

    def transcribe_answer(self, audio_file):
        return self.deepgram_api.transcribe_audio(audio_file_path=audio_file)

    def evaluate_answer(self, question, answer):
        feedback_prompt = self.prompt_generator.generate_feedback_prompt(
            question, answer
        )
        evaluation = self.groq_api.api_calls(feedback_prompt)

        if isinstance(evaluation, dict):
            self.total_score += evaluation.get("score", 0)
            return evaluation
        else:
            print("Error: Unexpected evaluation response:", evaluation)
            return {"score": 0, "feedback": "Error in evaluation"}


def countdown_timer(placeholder, duration):
    for remaining in range(duration, 0, -1):
        placeholder.text(f"Time remaining: {remaining} seconds")
        time.sleep(1)
    placeholder.empty()


def run_viva_step(app, question_display):
    if app.question_no <= app.max_questions:
        # Generate and display question
        app.generate_question()
        question_display.markdown(f"**Question:** {app.current_question}")

        # Synthesize and play question audio
        question_audio_path = os.path.join(
            "temp", f"question_{app.question_no}_audio.wav"
        )
        threading.Thread(
            target=app.synthesize_and_play_question,
            args=(app.current_question, question_audio_path),
        ).start()

        # Wait for audio to finish (you may need to adjust this time)
        time.sleep(5)

        # Start the countdown timer

        # Record answer
        answer_audio_path = os.path.join("temp", f"answer_{app.question_no}.mp3")
        app.record_answer(answer_audio_path)

        # Transcribe answer (display only in terminal)
        app.current_answer = app.transcribe_answer(answer_audio_path)
        print(f"User's answer: {app.current_answer}")

        # Evaluate answer
        evaluation = app.evaluate_answer(app.current_question, app.current_answer)
        app.evaluation_feedback = evaluation.get("feedback", "No feedback provided.")
        print(f"Feedback: {app.evaluation_feedback}")

        app.question_no += 1

        # Schedule the next question
        if app.question_no <= app.max_questions:
            time.sleep(2)  # Give some time before next question
            st.rerun()
    else:
        st.success(f"Viva complete! Total Score: {app.total_score}")


def main():
    st.set_page_config(page_title="Viva Automation - Question Answer", layout="wide")

    # Initialize VivaAutomationApp
    if "viva_app" not in st.session_state:
        st.session_state.viva_app = VivaAutomationApp()

    # Display subject name and question number
    st.title(f"{st.session_state.viva_app.subject} Viva")
    st.subheader(
        f"Question {st.session_state.viva_app.question_no}/{st.session_state.viva_app.max_questions}"
    )

    # Create placeholders for dynamic content
    question_display = st.empty()

    # Run the viva step
    run_viva_step(st.session_state.viva_app, question_display)


if __name__ == "__main__":
    main()
