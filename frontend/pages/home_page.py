# Streamlit UI for the homepage
# This Includes: title of the project, a section for instructions, a checkbox for agreement, and a submit button to proceed. 

import streamlit as st

class HomePage:
    def display(self):
        # Title of the project
        st.title("Viva Automation System")
        
        # Project introduction and instructions
        st.subheader("Welcome to the Viva Automation App")
        st.write("""
            This application automates the viva exam process by generating interactive questions, evaluating your answers, 
            and providing feedback based on your responses. Here’s how to get started:
            
            1. **Select Topics**: Begin by selecting the topics you want to be questioned on.
            2. **Answer Questions**: Questions will be asked, and you’ll need to answer verbally. The app will convert your speech into text.
            3. **Receive Feedback**: After a few questions, you’ll get feedback and a score based on your performance.
            
            **Note**: Ensure you have a working microphone, as this application will capture your responses verbally.
        """)

        # Checkbox for agreement
        agree = st.checkbox("I agree to the terms and conditions")

        # Submit button to proceed to the next page if agreed
        if st.button("Start", key="start_button"):
            if agree:
                # Setting session state to navigate to the next page
                st.session_state.current_page = "Topic Selection"  # Replace with the actual page name as per your app structure
            else:
                st.warning("Please agree to the terms and conditions before proceeding.")

        st.stop()

# Running the page in Streamlit (for standalone testing)
if __name__ == "__main__":
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"

    page = HomePage()
    page.display()
