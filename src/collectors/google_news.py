import requests
from bs4 import BeautifulSoup

def fetch_google_news(query="India", limit=10):
    """
    Fetch latest news from Google News RSS.
    100% free, no API, no region blocks.
    """
    url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}&hl=en-IN&gl=IN&ceid=IN:en"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "xml")

    items = soup.find_all("item")[:limit]

    news = []
    for item in items:
        news.append({
            "title": item.title.text,
            "content": item.description.text,
            "link": item.link.text,
            "date": item.pubDate.text,
            "source": "google_news"
        })

    return news


if __name__ == "__main__":
    print(fetch_google_news("US news", 5))
