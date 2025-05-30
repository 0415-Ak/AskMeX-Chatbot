from textblob import TextBlob


def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        return "😊 Positive"
    elif polarity < -0.1:
        return "😠 Negative"
    else:
        return "😐 Neutral"


def summarize_tweets(tweets):
    all_text = " ".join(tweet["text"] for tweet in tweets)
    blob = TextBlob(all_text)
    sentences = blob.sentences
    summary = " ".join(str(s) for s in sentences[:3])
    return summary
