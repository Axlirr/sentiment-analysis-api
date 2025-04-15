from transformers import pipeline
import torch

class SentimentAnalyzer:
    def __init__(self):
        self.sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model="nlptown/bert-base-multilingual-uncased-sentiment",
            device=0 if torch.cuda.is_available() else -1
        )
        
        self.emotion_pipeline = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            device=0 if torch.cuda.is_available() else -1
        )

    def analyze_sentiment(self, text: str) -> dict:
        # Get basic sentiment (1-5 stars)
        sentiment_result = self.sentiment_pipeline(text)[0]
        
        # Get detailed emotions
        emotion_result = self.emotion_pipeline(text)[0]
        
        # Convert 1-5 scale to sentiment labels
        sentiment_score = int(sentiment_result['label'][0])
        sentiment_mapping = {
            1: "very negative",
            2: "negative",
            3: "neutral",
            4: "positive",
            5: "very positive"
        }
        
        return {
            "text": text,
            "sentiment": sentiment_mapping[sentiment_score],
            "confidence": sentiment_result['score'],
            "emotion": emotion_result['label'],
            "emotion_score": emotion_result['score']
        }

# Initialize the model globally
analyzer = SentimentAnalyzer()