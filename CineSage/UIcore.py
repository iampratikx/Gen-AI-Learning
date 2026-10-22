
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_ollama import ChatOllama

st.set_page_config(page_title="🎬 Movie Info Extractor", layout="centered")

st.title("🎬 Movie Information Extractor")
st.write("Paste any movie description and AI will convert it into structured data.")

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
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        Extract movie information from the paragraph.
        {format_instructions}
        """
    ),
    ("human", "{paragraph}")
])

paragraph = st.text_area("Enter Movie Paragraph", height=200)

if st.button("Extract Data"):
    if not paragraph.strip():
        st.warning("Please enter a paragraph first.")
    else:
        with st.spinner("Analyzing movie..."):
            try:
                final_prompt = prompt.invoke({
                    "paragraph": paragraph,
                    "format_instructions": parser.get_format_instructions()
                })

                response = llm.invoke(final_prompt)

                st.subheader("Raw Model Output")
                st.code(response.content, language="json")

                movie_data = parser.parse(response.content)

                st.subheader("Structured Output")
                st.json(movie_data.model_dump())

                st.success("Extraction Completed Successfully!")

            except Exception as e:
                st.error("Failed to parse response or generate movie data.")
                st.exception(e)
