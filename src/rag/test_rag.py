import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from retriever import load_retriever
from rag_chain import answer_query

retriever = load_retriever()

question = "Give me the latest updates in GeoPolitics."
response = answer_query(question, retriever)

print("\nQUESTION:", question)
print("\nANSWER:", response)
