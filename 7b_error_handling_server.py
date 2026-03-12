from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Create the Flask app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # or a simple welcome page

@app.route("/emotionDetector")
def emotion_detector_route():
    # Get input text from request
    text_to_analyze = request.args.get('textToAnalyze')

    # Handle blank input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again."

    # Call the emotion detector function
    response = emotion_detector(text_to_analyze)

    # Handle case where emotion_detector returns None (e.g., status code 400)
    if response is None:
        return "Invalid text! Please try again."

    # Format output nicely
    formatted_response = (
        f"Anger: {response.get('anger', 0):.2f}, "
        f"Disgust: {response.get('disgust', 0):.2f}, "
        f"Fear: {response.get('fear', 0):.2f}, "
        f"Joy: {response.get('joy', 0):.2f}, "
        f"Sadness: {response.get('sadness', 0):.2f}, "
        f"Dominant Emotion: {response.get('dominant_emotion', 'N/A')}"
    )
    return formatted_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
