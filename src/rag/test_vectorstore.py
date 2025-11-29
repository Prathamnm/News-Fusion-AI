import sys
import os

# Add ../ to path so Python can find collectors and preprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from collectors.google_news import fetch_google_news
from preprocess.prepare_documents import to_documents
from rag.create_vectorstore import create_vectorstore

# 1. Fetch news
google_news = fetch_google_news("India news", 10)

# 2. Convert to documents
docs = to_documents(google_news)

# 3. Build vectorstore
create_vectorstore(docs)
