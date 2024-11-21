
import json
import os
from global_variables import GlobalVariable

class FilterQuestionBank:
    def __init__(self):
        self.gv = GlobalVariable()
        self.question_bank = None
        self.selected_topics = None
        self.filtered_questionbank = None
        
        self.load_qb()
        self.load_selected_topics()

    def load_qb(self):
        """Load the question bank JSON file."""
        try:
            with open(self.gv.question_bank) as f:
                self.question_bank = json.load(f)
        except FileNotFoundError:
            print(f"Error: {self.gv.question_bank} not found.")
        except json.JSONDecodeError:
            print(f"Error: Failed to decode {self.gv.question_bank}.")

    def load_selected_topics(self):
        """Load the selected topics from the JSON file."""
        try:
            with open(self.gv.selected_topics) as f:
                self.selected_topics = json.load(f)
        except FileNotFoundError:
            print(f"Error: {self.gv.selected_topics} not found.")
        except json.JSONDecodeError:
            print(f"Error: Failed to decode {self.gv.selected_topics}.")


    def fetch(self, question_bank):
        """
        Fetch specific questions based on the selected units and topics from the JSON file.
        
        Args:
        - question_bank (dict): The loaded question bank.

        Returns:
        - dict: A dictionary containing the questions for the selected units and topics.
        """
        # Initialize a dictionary to hold the fetched questions
        fetched_questions = {}

        # Iterate through each selected unit and topic
        for unit_name, topics in self.selected_topics.items():
            for unit in question_bank["Units"]:
                if unit["Unit Name"] == unit_name:
                    fetched_questions[unit_name] = {}
                    for topic in topics:
                        # Retrieve questions for the selected topics
                        if topic in unit["Topics"]:
                            fetched_questions[unit_name][topic] = unit["Topics"][topic]

        # Store the fetched questions in the attribute
        self.filtered_questionbank = fetched_questions

    def save_filtered_qb(self):
        """Save the filtered question bank to the temp folder."""
        # Ensure the 'temp' folder exists, if not, create it
        temp_folder = 'temp'
        os.makedirs(temp_folder, exist_ok=True)

        # Define the path for the filtered question bank JSON file
        filtered_qb_path = os.path.join(temp_folder, 'filtered_questionbank.json')

        # Save the filtered question bank as a JSON file
        with open(filtered_qb_path, 'w') as f:
            json.dump(self.filtered_questionbank, f, indent=4)

    def run(self):
        self.fetch(self.question_bank)
        self.save_filtered_qb()
        
if __name__ == "__main__":
    fq = FilterQuestionBank()
    fq.run()
