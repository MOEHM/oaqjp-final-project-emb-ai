from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        ## test joy
        self.assertEqual(emotion_detector('I am glad this happened')['dominant_emotion'], 'joy')
        ## test anger
        self.assertEqual(emotion_detector('I am angry')['dominant_emotion'], 'anger')
        ## test sadness
        self.assertEqual(emotion_detector('I am sad')['dominant_emotion'], 'sadness')
        ## test disgust
        self.assertEqual(emotion_detector('I am disgusted')['dominant_emotion'], 'disgust')
        ## test fear
        self.assertEqual(emotion_detector('I am afraid')['dominant_emotion'], 'fear')


unittest.main()