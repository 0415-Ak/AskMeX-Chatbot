import requests
import os
from dotenv import load_dotenv

load_dotenv()
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")


def create_url(query, max_results=10):
    query = query.replace(" ", "%10")
    return (
        f"https://api.twitter.com/2/tweets/search/recent"
        f"?query={query}&max_results={max_results}"
        f"&tweet.fields=created_at,author_id"
    )


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    r.headers["User-Agent"] = "TwitterQnABot"
    return r


def search_tweets(query):
    url = create_url(query)
    response = requests.get(url, auth=bearer_oauth)
    print("STATUS CODE:", response.status_code)
    print("RESPONSE:", response.text)

    if response.status_code != 200:
        return []

    tweets = response.json().get("data", [])
    results = []

    for tweet in tweets:
        tweet_id = tweet["id"]
        author_id = tweet["author_id"]
        tweet_text = tweet["text"]
        tweet_url = f"https://twitter.com/{author_id}/status/{tweet_id}"
        results.append({
            "text": tweet_text,
            "url": tweet_url
        })

    return results

if __name__ == "__main__":
    query = input("Enter your search topic: ")
    tweets = search_tweets(query)

    if not tweets:
        print("❌ No tweets found or API issue.")
    else:
        print(f"\n✅ Top {len(tweets)} tweets for: {query}\n")
        for i, tweet in enumerate(tweets, 1):
            print(f"{i}. {tweet['text']}\n🔗 {tweet['url']}\n{'-'*60}")
