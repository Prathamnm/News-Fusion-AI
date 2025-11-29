from collectors.google_news import fetch_google_news
from collectors.bbc_news import fetch_bbc_news
from collectors.cnn_news import fetch_cnn_news
from collectors.financialexpress_news import fetch_financialexpress_news
from collectors.aljazeera_news import fetch_aljazeera_news
from collectors.toi_news import fetch_toi_news

from preprocess.prepare_documents import to_documents
from rag.create_vectorstore import create_vectorstore


def update_news_vectorstore():
    print("📥 Fetching fresh daily news...")
    news = []

    # Google News categories
    categories = [
        ("India news", 12),
        ("World news", 12),
        ("Tech news", 12),
        ("Business news", 12)
    ]

    print("\n🌐 Fetching Google News...")
    for q, limit in categories:
        print(f"🔎 Google: {q}")
        news += fetch_google_news(q, limit)

    # Other sources
    print("\n📰 Fetching additional news sources...")

    print("🔎 BBC News...")
    news += fetch_bbc_news(12)

    print("🔎 CNN News...")
    news += fetch_cnn_news(12)

    print("🔎 Financial Express...")
    news += fetch_financialexpress_news(12)

    print("🔎 Al Jazeera...")
    news += fetch_aljazeera_news(12)

    print("🔎 Times of India...")
    news += fetch_toi_news(12)

    print(f"\n📊 Total collected articles: {len(news)}")

    print("\n🧹 Converting to documents...")
    docs = to_documents(news)

    print("🧠 Rebuilding vectorstore...")
    create_vectorstore(docs)

    print("\n✨ Daily update complete!")


if __name__ == "__main__":
    update_news_vectorstore()
