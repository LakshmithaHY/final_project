# Repository for final project
# Final Project – Emotion Detector

This repository contains the AI-based Emotion Detector application developed as part of the Final Project. 

## Project Description
The Emotion Detector is a web application that uses IBM Watson NLP to analyze text and identify emotions such as joy, anger, sadness, fear, and disgust.

## Features
- Emotion detection from user input text
- Web interface using Flask
- Error handling for blank or invalid inputs
- Unit tests included
- Packaged as a Python module for easy import

## Repository Structure
- `EmotionDetection/` – Python package with emotion detection logic
- `server.py` – Flask web server for deployment
- `test_emotion_detection.py` – Unit tests
- `templates/` and `static/` – Web UI files

## How to Run
1. Install dependencies: `pip3 install -r requirements.txt`
2. Start the server: `python3 server.py`
3. Open the app via lab proxy at port 5000
