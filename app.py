from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


# Function to get sentiment
def sentiment_analyze(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Sentiment based on polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, polarity, subjectivity


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    user_input = request.form["text"]
    sentiment, polarity, subjectivity = sentiment_analyze(user_input)
    return render_template("results.html",
                           text=user_input,
                           sentiment=sentiment,
                           polarity=polarity,
                           subjectivity=subjectivity)


if __name__ == "__main__":
    app.run(debug=True)
