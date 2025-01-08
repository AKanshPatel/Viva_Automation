import streamlit as st
import time
import threading
import os
import re  # For processing evaluation response text
from backend.prompt import PromptGenerator  # Custom Prompt Generator module
from backend.groq_api_llm import GroqApi  # Groq API for LLM calls
from backend.deepgram_stt_tts import DeepgramAPI  # Deepgram API for STT and TTS
from utils.audio import record_audio, play_audio 

def run_viva_step(app):
    # Initialize placeholders for dynamic updates
    question_placeholder = st.empty()
    answer_placeholder = st.empty()
    feedback_placeholder = st.empty()
    score_placeholder = st.empty()
    progress_placeholder = st.empty()

    # Generate question
    app.generate_question()
    st.session_state.current_question = app.current_question
    question_placeholder.markdown(
        f"**Question {app.question_no}/{app.max_questions}:** {app.current_question}"
    )

    # Synthesize and play question audio
    question_audio_path = os.path.join("temp", f"question_{app.question_no}_audio.wav")
    progress_placeholder.info("Playing the question audio...")
    threading.Thread(
        target=app.synthesize_and_play_question,
        args=(app.current_question, question_audio_path),
    ).start()

    # Allow time for audio to play
    time.sleep(5)  # Adjust this based on actual audio duration
    progress_placeholder.empty()  # Clear progress message

    # Record and transcribe answer
    progress_placeholder.info("Recording your answer...")
    answer_audio_path = os.path.join("temp", f"answer_{app.question_no}.mp3")
    app.record_answer(answer_audio_path)
    progress_placeholder.empty()  # Clear progress message

    # Display transcribed answer
    app.current_answer = app.transcribe_answer(answer_audio_path)
    st.session_state.current_answer = app.current_answer
    answer_placeholder.markdown(
        f"**Your Answer:** {st.session_state.current_answer}"
    )

    # Evaluate answer
    progress_placeholder.info("Evaluating your answer...")
    evaluation = app.evaluate_answer(app.current_question, app.current_answer)
    app.evaluation_feedback = evaluation.get("feedback", "No feedback provided.")
    app.total_score += evaluation.get("score", 0)

    # Update session state and placeholders
    st.session_state.current_feedback = app.evaluation_feedback
    st.session_state.current_score = app.total_score

    feedback_placeholder.markdown(
        f"**Feedback:** {st.session_state.current_feedback}"
    )
    score_placeholder.markdown(f"**Total Score:** {st.session_state.current_score}")
    progress_placeholder.empty()  # Clear progress message

    # Update question number
    app.question_no += 1
    if app.question_no > app.max_questions:
        st.session_state.viva_complete = True
    else:
        st.experimental_rerun()  # Rerun the app for the next question


def main():
    # Page configuration
    st.set_page_config(page_title="Viva Automation", layout="wide")

    # Initialize session state
    if "viva_app" not in st.session_state:
        st.session_state.current_question = ""
        st.session_state.current_answer = ""
        st.session_state.current_feedback = ""
        st.session_state.current_score = 0
        st.session_state.viva_complete = False

    app = st.session_state.viva_app

    # Title
    st.markdown(
        f"<h1 style='text-align: center;'>{app.subject} VIVA EXAM</h1>",
        unsafe_allow_html=True,
    )

    # Viva Content
    st.write(f"**Question Number:** {app.question_no}/{app.max_questions}")
    st.write(f"**Current Question:** {st.session_state.current_question or 'Waiting...'}")
    st.write(f"**Your Answer:** {st.session_state.current_answer or 'Recording...'}")
    st.write(f"**Feedback:** {st.session_state.current_feedback or 'Awaiting feedback...'}")
    st.write(f"**Total Score:** {st.session_state.current_score}")

    # End Button
    if st.session_state.viva_complete:
        if st.button("End Exam"):
            st.success("Viva Exam Completed.")
    else:
        run_viva_step(app)


if __name__ == "__main__":
    main()
