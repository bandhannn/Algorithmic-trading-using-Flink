import nltk

# Set the NLTK data path
nltk.data.path.append('/Users/bandhan/Desktop/nltk_data') 
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()


def get_sentiment(text):
    scores = sia.polarity_scores(text)
    return scores['compound']
