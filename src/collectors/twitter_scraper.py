import os
from dotenv import load_dotenv
import requests

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def fetch_tweets(query="India news", limit=10):
    """
    Fetch tweets using SerpAPI (100% works in India).
    Requires SERPAPI_KEY in .env
    """

    url = "https://serpapi.com/search.json"

    params = {
        "engine": "twitter",
        "q": query,
        "api_key": SERPAPI_KEY,
        "count": limit
    }

    try:
        res = requests.get(url, params=params)
        data = res.json()

        tweets = []

        for item in data.get("tweets", [])[:limit]:
            tweets.append({
                "content": item.get("text", ""),
                "username": item.get("user", {}).get("screen_name", ""),
                "date": item.get("timestamp", ""),
                "source": "twitter"
            })

        return tweets

    except Exception as e:
        print("Error:", e)
        return []


if __name__ == "__main__":
    print(fetch_tweets("India news", 5))
