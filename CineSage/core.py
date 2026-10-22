
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen3:4b-instruct-2507-q4_K_M",
    temperature=0.6,
    num_predict=512,
    num_ctx=4096,
    top_p=0.9,
    top_k=40,
    repeat_penalty=1.1,
)

class Movie(BaseModel):
    title: str 
    release_year : Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


parser = PydanticOutputParser(pydantic_object=Movie)


prompt = ChatPromptTemplate.from_messages([
    ('system',"""
Extract movie information from the paragraph
     {format_instructions}
"""),
("human","{paragraph}")
]
)


para = input("Give your paragraph : ")

final_prompt = prompt.invoke(
    {"paragraph" : para,
     'format_instructions': parser.get_format_instructions()
     }
)

response = llm.invoke(final_prompt)
movie_data = parser.parse(response.content)

print(movie_data)