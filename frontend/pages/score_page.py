import streamlit as st

class ScorePage:
    @staticmethod
    def show(navigate=None):
        st.title("Final Score & Feedback")
        
        # Sample data
        total_score = 50
        sample_score = 42  # Example final score
        questions_asked = 5
        correct_answers = 5  # Example number of correct answers
        incorrect_answers = questions_asked - correct_answers
        
        # Example data for questions, answers, and marks
        question_data = [
            {
                "question": "What is supervised learning?",
                "answer": "Supervised learning is a machine learning technique that uses labeled data sets to train algorithms to predict outcomes and recognize patterns",
                "score": 8,
            },
            {
                "question": "What is Knowledge Discovery in Databases (KDD)?",
                "answer": "KDD is the process of identifying patterns in data that are novel, potentially useful, and understandable.",
                "score": 8,
            },
            {
                "question": "What does SEMMA stand for?",
                "answer": "SEMMA stands for Sample, Explore, Modify, Model, and Assess.",
                "score": 10,
            },
            {
                "question": "What are labeled and unlabeled data?",
                "answer": "Labeled data has tags or labels that classify the data's elements or outcomes, while unlabeled data does not have any meaningful tags or labels",
                "score": 9,
            },
            {
                "question": "Give an example of unsupervised learning.",
                "answer": "Clustering algorithms like K-Means are examples of unsupervised learning.",
                "score": 7,
            },
        ]

        # Score Display
        st.subheader("Your Final Score")
        st.markdown(f"<h1 style='text-align: center; color: green;'>{sample_score}/{total_score}</h1>", unsafe_allow_html=True)

        # Feedback Display
        st.subheader("Feedback")
        sample_feedback = """
        - You have a strong understanding of core concepts. 💡
        - Try to elaborate more on examples in your answers. 📚
        - Work on improving accuracy in technical definitions. 🔍
        """
        st.write(sample_feedback)

        # Display Questions, Answers, and Scores
        st.subheader("Questions and Responses")
        for idx, q_data in enumerate(question_data, 1):
            st.write(f"**Q{idx}: {q_data['question']}**")
            st.write(f"**Your Answer:** {q_data['answer']}")
            st.write(f"**Score:** {q_data['score']}/10")
            st.markdown("---")

        # Number of questions asked
        st.subheader("Questions Summary")
        st.write(f"**Questions Asked:** {questions_asked}")
        st.write(f"**Correct Answers:** {correct_answers}")
        st.write(f"**Incorrect Answers:** {incorrect_answers}")

        # Option to restart the process or navigate
        st.markdown("---")
        st.write("Do you want to restart the process or end the session?")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Restart"):
                if navigate:
                    navigate("HomePage")  # Replace with actual navigation logic
                else:
                    st.experimental_rerun()  # Reload the app (useful in standalone mode)

        with col2:
            if st.button("End"):
                st.write("Thank you for participating!")  # Message for ending
                st.stop()  # Stop the Streamlit app

# Direct run for testing
if __name__ == "__main__":
    ScorePage.show()
