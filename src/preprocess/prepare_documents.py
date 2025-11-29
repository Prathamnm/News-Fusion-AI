from langchain_core.documents import Document
from preprocess.cleaner import clean_text

def to_documents(news_items):
    docs = []

    for item in news_items:
        title = clean_text(item.get("title", ""))
        content = clean_text(item.get("content", ""))

        full_text = f"{title}\n\n{content}"

        docs.append(
            Document(
                page_content=full_text,
                metadata={
                    "source": item.get("source", ""),
                    "link": item.get("link", ""),
                    "date": item.get("date", "")
                }
            )
        )

    return docs
