def answer_query(question, retriever):
    print("🔍 Retrieving docs...")
    docs = retriever.invoke(question)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
    Answer using only the context below:

    CONTEXT:
    {context}

    QUESTION: {question}
    """

    from llm.llm import ask_llm
    return ask_llm(prompt)
