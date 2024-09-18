from flask import Flask, request, jsonify, render_template
import sys
import os

# Add the project directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from Sentiment_Analysis.tw_sentiment import analyze_sentiment  # Import your sentiment analysis function

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    tweet = data['tweet']
    sentiment_result = analyze_sentiment(tweet)
    return jsonify(sentiment_result)

if __name__ == '__main__':
    app.run(debug=True)
