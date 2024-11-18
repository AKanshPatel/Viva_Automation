import streamlit as st
from frontend.pages.home_page import HomePage
from frontend.pages.topic_selection import TopicSelection
from frontend.pages.question_answer import QuestionAnswer
from frontend.pages.score_page import ScorePage

class MainControl:
    def __init__(self):
        # Initialize session state to track the current page
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 'HomePage'
            st.rerun()

    def navigate(self, page):
        # Update the current page and re-render
        st.session_state.current_page = page
        st.rerun()

    def run(self):
        # Display the current page based on the session state
        if st.session_state.current_page == 'HomePage':
            HomePage.show(self.navigate)
        elif st.session_state.current_page == 'TopicSelection':
            TopicSelection.show(self.navigate)
        elif st.session_state.current_page == 'QuestionAnswer':
            QuestionAnswer.show(self.navigate)
        elif st.session_state.current_page == 'ScorePage':
            ScorePage.show(self.navigate)

# Running the app
if __name__ == "__main__":
    control = MainControl()
    control.run()

