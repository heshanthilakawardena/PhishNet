# PhishNet - AI URL Threat Detection System

PhishNet is an AI-powered cybersecurity application that analyzes and classifies URLs based on potential security threats. It uses Google's Gemini AI model with a Flask web interface to identify URLs as legitimate, phishing, malware, or defacement.

## Features

- AI-based URL threat classification
- Real-time URL analysis
- Flask web application
- Secure API key handling using environment variables

## Technologies

- Python
- Flask
- Google Gemini API
- HTML/CSS

## Categories

- Legit: Safe and trusted websites
- Phishing: Fraudulent websites attempting to steal information
- Malware: Websites linked to malicious software
- Defacement: Compromised websites modified by attackers

## Setup

Install dependencies:

pip install -r requirements.txt

Create a `.env` file:

GOOGLE_API_KEY=your_api_key_here

Run the application:

python main.py

## Future Improvements

- Machine learning-based URL feature extraction
- Threat intelligence API integration
- Browser extension support

## Author

Heshan Thilakawardena
Cybersecurity Undergraduate
