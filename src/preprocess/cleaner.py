import re
from bs4 import BeautifulSoup

def clean_text(text: str) -> str:
    """Clean raw news text and return clean text."""
    if not text:
        return ""

    # Remove HTML tags if present
    text = BeautifulSoup(text, "html.parser").get_text()

    # Remove URLs
    text = re.sub(r'http\S+|www\.\S+', '', text)

    # Remove emojis
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)

    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()
