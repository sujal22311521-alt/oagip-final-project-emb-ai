import requests

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    response = requests.post(url, json=input_json, headers=headers)
    
    if response.status_code == 200:
        response_json = response.json()
        
        emotions = response_json['emotionPredictions'][0]['emotion']
        
        sadness = emotions['sadness']
        joy = emotions['joy']
        fear = emotions['fear']
        disgust = emotions['disgust']
        anger = emotions['anger']
        
        dominant_emotion = max(emotions, key=emotions.get)
        
        return f"For the given statement, the system response is 'sadness': {sadness}, 'joy': {joy}, 'fear': {fear}, 'disgust': {disgust}, 'anger': {anger}. The dominant emotion is {dominant_emotion}."
    
    else:
        return "Error in emotion detection"
