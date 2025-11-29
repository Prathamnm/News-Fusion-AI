import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

def ask_llm(prompt):
    client = InferenceClient(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        token=os.getenv("HUGGINGFACE_API_KEY")
    )

    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.7,
        top_p=0.9
    )

    return response.choices[0].message["content"]
