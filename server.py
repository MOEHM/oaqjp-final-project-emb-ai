from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask('Emotion Detection APP')

@app.route('/emotionDetector')
def emotion_detection():
    '''
    Function to detect emotions from a given text
    '''
    textToAnalyze = request.args.get('textToAnalyze')
    data = emotion_detector(textToAnalyze)


    return (f"""For the given statement, the system response is 
                'anger' : {data['anger']},
                'disgust' : {data['disgust']},
                'fear' : {data['fear']},
                'joy' : {data['joy']},
                'sadness' : {data['sadness']}.
                The dominant emotion is {data['dominant_emotion']}
            """
            )


@app.route('/')
def index():
    '''
    Function to return index.html main template
    '''
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)