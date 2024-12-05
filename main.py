import streamlit as st
import time
import os
from test_gpt import VivaAutomationApp


def main():
    st.set_page_config(
        page_title="Machine Learning Viva", page_icon="🎓", layout="wide"
    )
    st.title("Machine Learning Viva")

    # Initialize the VivaAutomationApp
    if "viva_app" not in st.session_state:
        st.session_state.viva_app = VivaAutomationApp()
        st.session_state.question_no = 1
        st.session_state.max_questions = 1
        st.session_state.viva_complete = False
        st.session_state.recording = False
        st.session_state.evaluating = False

    viva_app = st.session_state.viva_app

    if not st.session_state.viva_complete:
        # Display current question number
        st.subheader(
            f"Question {st.session_state.question_no}/{st.session_state.max_questions}"
        )

        # Generate and display the question
        if "current_question" not in st.session_state:
            viva_app.generate_question()
            st.session_state.current_question = viva_app.current_question

        st.write(st.session_state.current_question)

        # Play the question audio
        question_audio_path = os.path.join(
            "temp", f"question_{st.session_state.question_no}_audio.wav"
        )
        viva_app.synthesize_and_play_question(
            st.session_state.current_question, question_audio_path
        )
        st.audio(question_audio_path)

        # Record the answer
        if not st.session_state.recording and not st.session_state.evaluating:
            st.session_state.recording = True
            st.info("Recording your answer...")
            answer_audio_path = os.path.join(
                "temp", f"answer_{st.session_state.question_no}.mp3"
            )
            viva_app.record_answer(answer_audio_path)
            st.session_state.recording = False
            st.session_state.evaluating = True
            st.rerun()

        # Evaluate the answer
        if st.session_state.evaluating:
            st.info("Evaluating your answer...")
            answer_audio_path = os.path.join(
                "temp", f"answer_{st.session_state.question_no}.mp3"
            )
            viva_app.current_answer = viva_app.transcribe_answer(answer_audio_path)
            evaluation = viva_app.evaluate_answer(
                st.session_state.current_question, viva_app.current_answer
            )
            viva_app.evaluation_feedback = evaluation.get(
                "feedback", "No feedback provided."
            )

            # Display feedback
            st.write("Feedback:", viva_app.evaluation_feedback)

            # Move to the next question or complete the viva
            st.session_state.question_no += 1
            if st.session_state.question_no > st.session_state.max_questions:
                st.session_state.viva_complete = True
            else:
                # Clear the current question for the next iteration
                del st.session_state.current_question

            st.session_state.evaluating = False
            time.sleep(3)  # Give user time to read feedback
            st.rerun()

    else:
        # Display the total score when the viva is complete
        st.success(f"Viva complete! Total Score: {viva_app.total_score}")


if __name__ == "__main__":
    main()
