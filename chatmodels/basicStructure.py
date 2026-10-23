
from dotenv import load_dotenv
#load APis from .env file
load_dotenv()

# used for any open sourse LLm model
# not need to mension specific model
from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-4.1")

response = model.invoke("what is cricket?")

print(response.content)