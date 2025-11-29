from prepare_documents import to_documents

dummy_news = [
    {
        "title": "India wins major award",
        "content": "This is a big achievement for the country.",
        "source": "google_news",
        "link": "https://example.com",
        "date": "2025-11-21"
    }
]

docs = to_documents(dummy_news)
print(docs)
