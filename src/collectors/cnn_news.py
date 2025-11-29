import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_cnn_news(limit=10):
    url = "http://rss.cnn.com/rss/edition.rss"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "xml")

    items = soup.find_all("item")[:limit]

    articles = []
    for item in items:
        title = item.title.text if item.title else ""
        
        # CNN often has <description/> or missing content
        description = ""
        if item.description and item.description.text:
            description = item.description.text
        elif item.find("content:encoded"):
            description = item.find("content:encoded").text
        else:
            description = title  # fallback

        link = item.link.text if item.link else ""
        date = item.pubDate.text if item.pubDate else str(datetime.utcnow())

        articles.append({
            "title": title,
            "content": description,
            "source": "cnn",
            "link": link,
            "date": date
        })

    return articles


if __name__ == "__main__":
    print(fetch_cnn_news(5))
