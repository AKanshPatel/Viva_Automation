
# Project Overview!

## WorkFlow

![Flow Chart](https://github.com/user-attachments/assets/a8c49b87-c87c-49b9-8a4f-8d2e9698291e)


# Project Overview

This project contains the following folder structure:

## Folder Structure

```plaintext
project_root/
│
├── app.py                           # Main Streamlit app entry point
├── requirements.txt                 # Project dependencies
├── README.md                        # Basic project overview
│
├── data/                            # Stores data files
│   └── question_bank.json           # JSON file with pre-set questions and topics
│
├── documents/                       # Documentation assets
│   ├── diagrams/                    # Technical diagrams and flowcharts
│   │   ├── architecture.png         # System architecture diagram
│   │   ├── workflow.png             # Workflow or sequence diagram
│   │   └── components.png           # Diagram of components and interactions
│   └── images/                      # Additional images for documentation
│       ├── ui_example.png           # Example screenshot of Streamlit UI
│       └── data_flow.png            # Data flow diagram
│
├── src/                             # Core backend code
│   ├── prompt.py                    # It will deal with the prompts                        
│   ├── groq_api.py                  # For API calls
│   ├── text_to_speech.py            # Converts text to audio (TTS)
│   ├── speech_to_text.py            # Converts audio to text (STT)
│   └── evaluation.py                # Evaluates answers using GROQ API
│
├── frontend/                        # Frontend components for Streamlit
│   ├── main_control.py              # Controls the navigation and page flow
│   └── pages/                       # Individual page components
│       ├── home_page.py             # Home page with title and instructions
│       ├── topic_selection.py       # Topic selection page
│       ├── question_answer.py       # Question and answer page
│       └── score_page.py            # Final score and feedback page
│
├── utils/                           # Heplper functions and utilities
│   ├── global_variable.py           # Store Global Variable
│   └── fetch_questions.py           # Filter the Question Bank for prompt 
│
├── temp/                            # Temporary storage
    ├── selected_topics.json         # Stores the selected topics of the user
    └── filtered_questionbank.json   # Stores the selected questions of the user