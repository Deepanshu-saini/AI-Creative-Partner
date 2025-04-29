#!/bin/bash

# Activate the virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install dependencies
poetry install

# Run the Streamlit app
streamlit run streamlit_app.py 