from llm import ask_llm

print("Sending LLM request...")
resp = ask_llm("Write a one-line motivational quote.")
print("\nResponse:")
print(resp)
