from cleaner import clean_text

raw = """
<a href="https://news.google.com">Breaking news:</a> 
India wins big 🚀🔥🔥 
More on: https://example.com 
"""

cleaned = clean_text(raw)
print(cleaned)
