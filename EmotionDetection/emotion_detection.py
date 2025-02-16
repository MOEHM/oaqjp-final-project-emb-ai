import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=data)

    ## Format the output
    response_json = json.loads(response.text)
    emotion_data = response_json['emotionPredictions'][0]['emotion']
    anger = emotion_data.get('anger')
    disgust = emotion_data.get('disgust')
    fear = emotion_data.get('fear')
    joy = emotion_data.get('joy')
    sadness = emotion_data.get('sadness')
    dominant_emotion = max(anger, disgust, fear, joy, sadness)


    emotions = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
        # "dominant_emotion": dominant_emotion
    }

    dominant_emotion = max(emotions, key=emotions.get)

    data = {
         "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }

    return data

# print(emotion_detector('i love this technology'))