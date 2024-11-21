
import streamlit as st

class ScorePage:
    @staticmethod
    def show(navigate=None):
        st.title("Score Page")
        
        # Display a message or the final score here
        st.write("Your final score and feedback will be displayed here.")

        # Option to restart the process
        if st.button("End"):
            if navigate:
                # If navigating within a larger app, go to HomePage or reset logic
                navigate("HomePage")  # or any other page to reset
            else:
                # Directly stop the app for standalone mode
                st.stop()

# Direct run for testing
if __name__ == "__main__":
    ScorePage.show()
