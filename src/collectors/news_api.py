import requests
from dotenv import load_dotenv
import os

# Load your NewsAPI key from the .env file
load_dotenv()
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

def fetch_news(limit=5, country="us"):  # 'us' is for United States; change to any ISO country code
    url = f"https://newsapi.org/v2/top-headlines?country={country}&pageSize={limit}&apiKey={NEWSAPI_KEY}"
    res = requests.get(url)
    print("Status code:", res.status_code)
    data = res.json()
    print("Raw JSON:", data) # Debug output for troubleshooting

    articles = data.get("articles", [])
    return [
        {
            "title": a.get("title", ""),
            "content": a.get("description", "") or "",
            "source": "newsapi"
        }
        for a in articles
    ]

if __name__ == "__main__":
    news_list = fetch_news(limit=5, country="us")  # Change 'country' as needed
    for news in news_list:
        print(f"Title: {news['title']}")
        print(f"Content: {news['content']}\n")

