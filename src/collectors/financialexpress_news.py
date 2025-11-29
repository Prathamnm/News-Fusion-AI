import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_financialexpress_news(limit=10):
    url = "https://www.financialexpress.com/feed/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "xml")

    items = soup.find_all("item")[:limit]

    articles = []
    for item in items:
        articles.append({
            "title": item.title.text,
            "content": item.description.text,
            "source": "financialexpress",
            "link": item.link.text,
            "date": item.pubDate.text if item.pubDate else str(datetime.utcnow())
        })

    return articles
