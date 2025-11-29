from news_api import fetch_news, NEWSAPI_KEY

print("Loaded API key:", NEWSAPI_KEY)
news = fetch_news()
print(news)
