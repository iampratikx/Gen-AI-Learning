
from dotenv import load_dotenv

load_dotenv()


# OpenAI
# from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model = "gpt-4.1")
# model = init_chat_model("gpt-4.1")

print(model)

response = model.invoke("what is cricket?")

print(response.content)


# GEMINI- Google

# from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI

# model = init_chat_model("google_genai:gemini-3.7-flash")
model = ChatGoogleGenerativeAI(model = "google_genai:gemini-3.7-flash")

response = model.invoke("Give me a paragraph on Machine Learning?")
print(response.content)

# GROQ 

from langchain_groq import ChatGroq
model = ChatGroq(model = "qwen/qwen3.8-27b")

response = model.invoke("What is Cricket?")
print(response.content)

# Mistral 
from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(model = "mistral-small-2506", temperature=0.9, max_tokens=20)

response = model.invoke("write a poem on AI")
print(response.content)




