# # 2nd page of the UI
# # Dropdowns for topic selection
import streamlit as st
import json

class TopicSelection:
    def __init__(self, json_file):
        self.json_file = json_file 
        self.question_bank = self.load_question_bank()
        self.unit_topics = self.extract_units_and_topics()

    def load_question_bank(self):
        """Load the question bank JSON file."""
        with open(self.json_file) as f:
            return json.load(f)
    
    def extract_units_and_topics(self):
        """Extract units and topics from the question bank, ignoring the questions."""
        return {
            unit["Unit Name"]: unit for unit in self.question_bank["Units"]
        }

    @staticmethod
    def show(navigate = None):
        # Initialize TopicSelection class with the question bank JSON file
        topic_selector = TopicSelection('data/question_bank.json')

        # Title
        st.title("From which unit/topic do you want us to question you:")

        # Heading 1: Select Unit
        st.header("Select Unit:")
        selected_units = st.multiselect("Choose Unit(s):", list(topic_selector.unit_topics.keys()))

        # Heading 2: Select Topics based on Unit
        selected_topics = {}

        for unit in selected_units:
            topics = list(topic_selector.unit_topics[unit]["Topics"].keys())  # Fetch topics for the selected unit
            
            # If any unit is selected, select all topics by default
            selected = st.multiselect(f"{unit} Topics:", topics, default=topics)
            selected_topics[unit] = selected  # Store the selected topics

        # Submit button
        if st.button("Submit"):
            # Create the dictionary {'Unit Name': [Topics, ...]}
            selected_dict = {unit: selected_topics[unit] for unit in selected_units}

            # Write the selected topics to JSON file
            with open("temp/selected_topics.json", "w") as f:
                json.dump(selected_dict, f, indent=4)

            # Set the session state to navigate to the QuestionAnswer page
            if navigate: 
                navigate("QuestionAnswer")
            else:
                st.session_state.current_page = 'QuestionAnswer'
                st.rerun()

if __name__ == "__main__":
    TopicSelection.show()