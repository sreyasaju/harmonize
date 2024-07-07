#!/bin/bash

# checking if python exists
python3 --version
if [ $? -ne 0 ]; then
    echo "Python not found. Please install Python 3.12."
    exit 1
fi

# creating and activating virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install aubio

echo "Installation Complete..."