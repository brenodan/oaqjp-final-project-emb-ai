"""
Emotion Detection Flask Server

This Flask server provides an API endpoint to detect emotions in text using the Watson NLP Library.

Example request:
    /emotionDetector
    {
        "text": "I am feeling very happy today!"
    }

Example response:
    {
        'anger': 0.1,
        'disgust': 0.2,
        'fear': 0.3,
        'joy': 0.4,
        'sadness': 0.5,
        'dominant_emotion': 'sadness'
    }

"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def detect_emotion():
    """
    Endpoint to detect emotions from a given text.

    This function receives a payload containing a 'text' field. 
    It processes the text using the `emotion_detector` function to determine 
    the levels of various emotions (i.e., anger, disgust, fear, joy, sadness) 
    and identifies the dominant emotion.

    Request format:
        /detect_emotion
        Content-Type: application/json
        {
            "text": "Your text to analyze here."
        }

    Response format:
        {
            'anger': <float>,
            'disgust': <float>,
            'fear': <float>,
            'joy': <float>,
            'sadness': <float>,
            'dominant_emotion': '<emotion>'
        }
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    part1 = f"For the given statement, the system response is 'anger': {result['anger']}, "
    part2 = f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
    part3 = f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
    part4 = f"The dominant emotion is {result['dominant_emotion']}."

    return_str = part1 + part2 + part3 + part4

    return return_str

@app.route("/")
def render_index_page():
    """
    Function for rendering the landing page using the provided template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
