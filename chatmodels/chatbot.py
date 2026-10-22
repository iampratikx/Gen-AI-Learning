
from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

try:
    llm = ChatOllama(
        model="qwen3:4b-instruct-2507-q4_K_M",
        temperature=0.6,
        num_predict=512,
        num_ctx=4096,
        top_p=0.9,
        top_k=40,
        repeat_penalty=1.1,
    )

    while True:
        choice = input(
            "Enter your choice (Funny=1, Sad=2, Happy=3): "
        ).strip()

        if choice == "1":
            mode = "You are a funny AI Agent."
            break
        elif choice == "2":
            mode = "You are a sad AI Agent."
            break
        elif choice == "3":
            mode = "You are a happy AI Agent."
            break
        else:
            print("Wrong choice! Please enter 1, 2, or 3.")

    message = [
        SystemMessage(content=mode)
    ]

    print(f"\nSelected mode: {mode}")
    print("Welcome! Type 0 to exit.")

    while True:
        prompt = input("You: ").strip()

        if prompt == "0":
            print("Goodbye!")
            break

        if not prompt:
            print("Please enter a message.")
            continue

        message.append(HumanMessage(content=prompt))

        response = llm.invoke(message)
        message.append(AIMessage(content=response.content))

        print("Bot:", response.content.strip())

except KeyboardInterrupt:
    print("\nProgram stopped by user.")

except Exception as e:
    print(f"\nAn error occurred: {type(e).__name__}: {e}")
