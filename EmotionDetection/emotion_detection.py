import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = input_json, headers = headers)
    response_json = json.loads(response.text)

    emotions = {}

    if response.status_code == 400:
        emotions = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    else:
        emotions = response_json['emotionPredictions'][0].get('emotion', {}) 
        emotion_scores = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores['dominant_emotion'] = dominant_emotion
        emotions = emotion_scores
    

    return emotions