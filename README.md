
# Project Overview!

## WorkFlow

![Flow Chart](https://github.com/user-attachments/assets/a8c49b87-c87c-49b9-8a4f-8d2e9698291e)


# Project Overview

This project contains the following folder structure:

## Folder Structure

```plaintext
VivaAutomation/
│
├── app.py                      # Main entry point for running the app
├── backend/                    # Contains all backend logic and models
│   ├── __init__.py
│   ├── question_generator.py   # Handles question generation using Groq API
│   ├── answer_evaluator.py     # Processes answers and interacts with Groq API
│   ├── api_calls.py            # Utility for making Groq and Deepgram API calls
│   ├── database.py             # Manages interactions with the database (scores, feedback)
│   └── utils/                  # Utility functions for backend
│       ├── topic_utils.py      # Fetch topics and pre-defined questions
│       └── feedback_utils.py   # Functions for processing feedback
│
├── frontend/                   # Contains all frontend logic and UI components
│   ├── navigation.py           # This File will handle the navigation between the pages
│   └── pages
│        ├── home_page.py            # UI for the home page
│        ├── topic_selection.py      # UI for selecting topics
│        ├── question_answer.py      # UI for question display, audio, and mic recording
│        └── score.py                # UI for showing the score and feedback
│
│
├── data/                       # Contains data files, such as question bank and scores
│   ├── question_bank.json      # The file containing the units, topics, and questions
│   └── scores.db               # Database for storing scores and feedback
├── documents/                  # Documentation assets
│   ├── diagrams/               # Technical diagrams and flowcharts
│   │   ├── architecture.png    # System architecture diagram
│   │   ├── workflow.png        # Workflow or sequence diagram
│   │   └── components.png      # Diagram of components and interactions
│   └── images/                 # Additional images for documentation
│       ├── ui_example.png      # Example screenshot of Streamlit UI
│       └── data_flow.png       # Data flow diagram
│
├── requirements.txt            # List of dependencies required for the project
└── README.md                   # Project documentation
