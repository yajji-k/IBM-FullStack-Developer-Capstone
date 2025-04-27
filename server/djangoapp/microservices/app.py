from flask import Flask, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer
import logging

app = Flask("Sentiment Analyzer")
sia = SentimentIntensityAnalyzer()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def home():
    return ("Welcome to the Sentiment Analyzer. Use /analyze/text to get the sentiment.")  # noqa: E501


@app.route('/analyze/<input_txt>', methods=['GET'])
def analyze_sentiment(input_txt):
    if not input_txt:
        logger.warning("No input text provided.")
        return jsonify({"error": "Input text is required."}), 400

    try:
        scores = sia.polarity_scores(input_txt)
        pos = float(scores['pos'])
        neg = float(scores['neg'])
        neu = float(scores['neu'])
        res = "positive"

        if neg > pos and neg > neu:
            res = "negative"
        elif neu > neg and neu > pos:
            res = "neutral"

        return jsonify({"sentiment": res})

    except Exception as e:
        logger.error(f"Error analyzing sentiment: {e}")
        return jsonify({
            "error": "An error occurred during sentiment analysis."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
