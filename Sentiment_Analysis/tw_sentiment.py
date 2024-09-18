from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

def preprocess_tweet(tweet):
    tweet_words = []
    for word in tweet.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        elif word.startswith('http'):
            word = "http"
        tweet_words.append(word)
    return " ".join(tweet_words)

# Load model and tokenizer globally to avoid reloading them for each request
roberta = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)
labels = ['Negative', 'Neutral', 'Positive']

def analyze_sentiment(tweet):
    tweet_proc = preprocess_tweet(tweet)
    encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
    output = model(**encoded_tweet)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    
    result = {labels[i].lower(): round(float(scores[i]) * 100, 2) for i in range(len(scores))}
    return result

if __name__ == "__main__":
    tweet = 'it heartbreaking about the news !!'
    print(analyze_sentiment(tweet))
