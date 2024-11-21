import streamlit as st

def question_answer_ui():
    # Header Section
    st.title("Interactive Viva")
    st.subheader("Answer the question below to proceed.")

    # Question Display Section
    question_text = "Explain the principle of Newton's First Law of Motion."
    st.markdown(f"**Question:** {question_text}")
    if st.button("Play Question Audio"):
        st.audio("path/to/question_audio.mp3")  # Replace with actual audio path
    
    # Answer Recording Section
    st.markdown("### Record Your Answer")
    if st.button("🎤 Start Recording"):
        st.markdown("Recording... (Indicator here)")  # Simulate recording
    if st.button("Submit Answer"):
        st.markdown("Processing your answer...")  # Simulate submission
    
    # Answer Processing and Feedback Section
    feedback_placeholder = st.empty()
    score_placeholder = st.empty()
    with st.spinner("Evaluating your answer..."):
        # Simulated feedback and score
        feedback = "Good explanation of the law but missed examples."
        score = 7.5
        feedback_placeholder.markdown(f"**Feedback:** {feedback}")
        score_placeholder.metric("Score", score)

    # Navigation Section
    st.button("Next Question")
    st.button("Exit Viva")

    # Progress Tracker
    progress = 2  # Example: Question 2 out of 6
    st.progress(progress / 6)
    st.markdown(f"Question {progress} of 6")

question_answer_ui()