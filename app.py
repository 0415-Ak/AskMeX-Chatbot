import streamlit as st
from twiter_api import search_tweets
from summary import summarize_tweets, get_sentiment

st.set_page_config(page_title="AskMeX - Twitter QnA", page_icon="🐦", layout="centered")
st.title("🐦 AskMeX – Twitter Q&A Bot")

query = st.text_input("Ask about any topic trending on Twitter:")

if query:
    with st.spinner("Searching Twitter..."):
        tweets = search_tweets(query)

    if tweets:
        st.subheader("🔍 Summary of Tweets")
        summary = summarize_tweets(tweets)
        st.success(summary)

        st.subheader("📈 Sentiment Analysis on Recent Tweets")
        for tweet in tweets[:5]:
            sentiment = get_sentiment(tweet["text"])
            st.markdown(f"**{sentiment}** → {tweet['text']}")
            st.markdown(f"[🔗 View Tweet]({tweet['url']})", unsafe_allow_html=True)
    else:
        st.error("No tweets found or API limit reached.")
