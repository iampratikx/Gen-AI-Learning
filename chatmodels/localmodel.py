from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline, HuggingFaceEndpoint


llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 128,
        "do_sample": True,
        "temperature": 0.7,
    },
)

question = input("You : ")

print("Question:", question)
print("Generating answer...")

response = llm.invoke(question)

print("Answer:", response)

