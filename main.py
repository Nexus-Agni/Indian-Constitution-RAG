from LLM_Calling import LLM_calling
from RAG import RAG_application

query = input("🤖 Enter your question: ")

context_text = RAG_application(query)

result = LLM_calling(query=query, context_text=context_text)
print(result)