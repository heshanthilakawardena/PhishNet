from flask import Flask, render_template, request
from google import genai
import os
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)

# Load API key from .env
load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini model
model = "gemini-2.0-flash"


# Function to classify URL
def url_detection(url):
    prompt = f"""
    You are an advanced AI model specializing in URL security classification.

    Analyze the given URL and classify it as one of the following categories:

    1. legit — safe and trusted websites
    2. phishing — fraudulent websites that steal personal data
    3. malware — sites distributing malicious software
    4. defacement — hacked or defaced sites

    URL: {url}

    Return only the class name in lowercase.
    """

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt
        )

        classification = response.text.strip().lower()

        # Normalize output
        if classification == "benign":
            classification = "legit"

        return classification

    except Exception as e:
        return f"error: {e}"


# Routes
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict_url():
    url = request.form.get('url', '').strip()

    if not url.startswith(("http://", "https://")):
        return render_template(
            "index.html",
            message="Invalid URL format.",
            input_url=url
        )

    classification = url_detection(url)

    return render_template(
        "index.html",
        input_url=url,
        predicted_class=classification
    )


if __name__ == '__main__':
    app.run(debug=True)