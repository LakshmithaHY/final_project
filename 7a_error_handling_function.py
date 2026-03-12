import requests

def emotion_detector(text_to_analyze):
    """
    Sends text to the Watson NLP service and returns the emotion analysis.
    Returns None if the request fails with a 400 status code.
    """
    if not text_to_analyze:
        # Return None if input is blank
        return None

    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/v1/analyze?version=2021-08-01"
    api_key = "YOUR_WATSON_API_KEY"

    # Prepare the request payload
    myobj = {
        "text": text_to_analyze,
        "features": {
            "emotion": {}
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Send POST request
    response = requests.post(url, json=myobj, headers=headers)

    # Handle 400 status code
    if response.status_code == 400:
        return None

    # Raise exception for other HTTP errors
    response.raise_for_status()

    # Parse the response JSON
    data = response.json()
    
    # Extract emotions
    emotions = data.get("emotion", {}).get("document", {}).get("emotion", {})
    
    # Add dominant emotion
    if emotions:
        emotions["dominant_emotion"] = max(emotions, key=emotions.get)

    return emotions
