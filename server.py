"""
This is the Flask server for the Sentiment Analysis application.
It provides a web interface to analyze the sentiment of user-provided text.
"""
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Analyzes the sentiment of text provided in the request arguments.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Handle empty input explicitly
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid input! The text field cannot be empty."

    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']

    if label is None:
        return "Invalid input! Try again with different text."

    # Format the final successful response string
    sentiment = label.split('_')[1].lower()
    return f"The text has been identified as **{sentiment}** with a score of {score:.4f}."

@app.route("/")
def render_index_page():
    """
    Renders the main index page of the web application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)