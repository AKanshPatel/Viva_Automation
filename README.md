
# Project Overview!

## WorkFlow
[Flow Chart](https://github.com/user-attachments/assets/a8c49b87-c87c-49b9-8a4f-8d2e9698291e)


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
├── docs/                            # Documentation assets
│   ├── diagrams/                    # Technical diagrams and flowcharts
│   │   ├── architecture.png         # System architecture diagram
│   │   ├── workflow.png             # Workflow or sequence diagram
│   │   └── components.png           # Diagram of components and interactions
│   └── images/                      # Additional images for documentation
│       ├── ui_example.png           # Example screenshot of Streamlit UI
│       └── data_flow.png            # Data flow diagram
│
├── src/                             # Core backend code
│   ├── question_generation.py       # Generates prompt and interacts with GROQ API
│   ├── text_to_speech.py            # Converts text to audio (TTS)
│   ├── speech_to_text.py            # Converts audio to text (STT)
│   └── evaluation.py                # Evaluates answers using LLM
│
├── config/                          # Configuration for API keys and settings
│   └── config.yaml                  # Stores configuration data like API keys
│
└── frontend/                        # Frontend components for Streamlit
    └── layout.py                    # Manages basic layout for Streamlit UI

