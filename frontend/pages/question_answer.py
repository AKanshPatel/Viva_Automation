# import streamlit as st

# class QuestionAnswer:
#     def display(self):
#         st.title("Question and Answer Page")


import streamlit as st

class QuestionAnswer:
    @staticmethod
    def show(navigate = None):
        st.title("Question and Answer Page")
        
        # Display a question here
        st.write("This is where questions will be displayed, and you can provide your answers.")

        # Add a Next button to proceed to the Score Page
        if st.button("Next"):
            if navigate:
                navigate("ScorePage")
            else:
                # Directly update session state and re-run
                st.session_state.current_page = "ScorePage"
                st.rerun()
                
if __name__ == "__main__":
    QuestionAnswer.show()