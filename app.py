from flask import Flask, request, jsonify, render_template
from sentiment_analysis.tw_sentiment import analyze_sentiment

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data or "tweet" not in data:
        return jsonify({"error": "Tweet text is required"}), 400

    tweet = data["tweet"]
    result = analyze_sentiment(tweet)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
