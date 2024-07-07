#!/bin/bash

# checking if python exists
python3 --version
if [ $? -ne 0 ]; then
    echo "Python not found. Please install Python 3.12."
    exit 1
fi

# installing packages required to build aubio
brew install pkg-config libsndfile fftw

# creating and activating virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Clone aubio repository
git clone https://github.com/aubio/aubio.git
cd aubio

# Build and install aubio
make
pip install setuptools
./setup.py build
pip install .

# Installation completed
echo "Installation Complete..."