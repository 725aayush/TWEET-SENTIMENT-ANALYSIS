from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import torch

def preprocess_tweet(tweet):
    tweet_words = []
    for word in tweet.split():
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        elif word.startswith('http'):
            word = 'http'
        tweet_words.append(word)
    return " ".join(tweet_words)

roberta = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(roberta)
model = AutoModelForSequenceClassification.from_pretrained(roberta)
labels = ['negative', 'neutral', 'positive']

def analyze_sentiment(tweet):
    tweet_proc = preprocess_tweet(tweet)
    encoded = tokenizer(tweet_proc, return_tensors="pt")

    with torch.no_grad():
        output = model(**encoded)

    scores = softmax(output.logits[0].numpy())
    return {labels[i]: round(float(scores[i]) * 100, 2) for i in range(3)}
