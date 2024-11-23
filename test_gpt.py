import re
import os
import time
from backend.prompt import PromptGenerator
from backend.groq_api import GroqApi
from backend.deepgram_new import DeepgramAPI
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
        self.max_questions = 2  # Set the maximum number of questions
        self.sleep_duration = 1 # Sleep duration after asking a question

    def generate_question(self):
        """
        Generates the first question or a subsequent question using the PromptGenerator module.
        """
        if self.question_no == 1:
            prompt = self.prompt_generator.generate_first_question_prompt()
        else:
            prompt = self.prompt_generator.generate_subsequent_question_prompt(
                self.current_question, self.current_answer, self.evaluation_feedback
            )
        self.current_question = self.groq_api.api_calls(prompt)

    def synthesize_and_play_question(self, question_text, output_file):
        """
        Converts text to speech and plays the audio.

        Args:
            question_text (str): The question text to be converted to speech.
            output_file (str): Path where the audio file will be saved.
        """
        self.deepgram_api.text_to_speech(text=question_text, output_file_path=output_file)
        play_audio(output_file)

    def record_answer(self, output_file):
        """
        Records the candidate's response and saves it as an audio file.

        Args:
            output_file (str): Path where the recorded answer will be saved.
        """
        time.sleep(2)
        record_audio(file_path=output_file)

    def transcribe_answer(self, audio_file):
        """
        Converts recorded speech to text.

        Args:
            audio_file (str): Path of the recorded answer audio file.

        Returns:
            str: Transcribed text of the answer.
        """
        return self.deepgram_api.transcribe_audio(audio_file_path=audio_file)

    def evaluate_answer(self, question, answer):
        """
        Evaluates the candidate's answer using Groq API.

        Args:
            question (str): The question text.
            answer (str): The candidate's answer.

        Returns:
            dict: A dictionary containing feedback and score.
        """
        feedback_prompt = self.prompt_generator.generate_feedback_prompt(question, answer)
        evaluation = self.groq_api.api_calls(feedback_prompt)
        
        # Attempt to parse the response if it's not a dictionary
        if isinstance(evaluation, str):
            # Parse the custom structure using regular expressions
            score_match = re.search(r'score:\s*(\d+)', evaluation)
            feedback_match = re.search(r'feedback:\s*"(.*?)"', evaluation, re.DOTALL)

            if score_match and feedback_match:
                score = int(score_match.group(1))
                feedback = feedback_match.group(1)
                self.total_score += score
                return {'score': score, 'feedback': feedback}
            else:
                print("Error: Unable to parse the evaluation response:", evaluation)
                return {'score': 0, 'feedback': "Error in evaluation"}
        elif isinstance(evaluation, dict):
            # If it's already a dictionary
            self.total_score += evaluation.get('score', 0)
            return evaluation
        else:
            # Handle unexpected response types
            print("Error: Groq API returned an unexpected response:", evaluation)
            return {'score': 0, 'feedback': "Error in evaluation"}

    def run(self):
        """
        Runs the Viva Automation process step-by-step.
        """
        while self.question_no <= self.max_questions:
            print(f"\nStarting Question {self.question_no}...")

            # Step 1: Generate and display the question
            self.generate_question()
            print(f"Question {self.question_no}: {self.current_question}")  # Display the question
            question_audio_path = os.path.join("temp", f"question_{self.question_no}_audio.wav")
            self.synthesize_and_play_question(self.current_question, question_audio_path)

            # Sleep for the specified duration before proceeding
            time.sleep(self.sleep_duration)

            # Step 2: Record and process the candidate's answer
            answer_audio_path = os.path.join("temp", f"answer_{self.question_no}.mp3")
            self.record_answer(answer_audio_path)
            self.current_answer = self.transcribe_answer(answer_audio_path)
            print(f"Answer {self.question_no}: {self.current_answer}")  # Display the transcribed answer

            # Step 3: Evaluate the answer
            evaluation = self.evaluate_answer(self.current_question, self.current_answer)
            self.evaluation_feedback = evaluation.get('feedback', "No feedback provided.")
            print(f"Feedback for Question {self.question_no}: {self.evaluation_feedback}")

            self.question_no += 1

        print(f"\nViva complete! Total Score: {self.total_score}")

if __name__ == "__main__":
    app = VivaAutomationApp()  # You can set the desired sleep duration here
    app.run()
