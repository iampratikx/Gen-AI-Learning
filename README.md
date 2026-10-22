# Generative AI Learning Repository

This repository contains my practice code and hands-on implementations while learning Generative AI concepts and tools using Python.

## 📚 Topics Covered

- **LLM Chatbots:** Building chatbot applications using different language models.
- **Local LLMs:** Experimenting with locally running language models using Ollama.
- **Hugging Face Models:** Exploring language models and their integration with Python applications.
- **Text Embeddings:** Generating text embeddings using embedding models.
- **CineSage:** Developing a movie-related AI application.
- **Python Application Development:** Building interactive applications using Streamlit.
- **API Integration:** Practicing integrations with AI model providers.

## 📂 Repository Structure

```text
Gen-AI-Learning/
├── CineSage/
│   ├── UIcore.py
│   └── core.py
├── chatmodels/
│   ├── UIchatbot.py
│   ├── chat.py
│   ├── chatbot.py
│   ├── huggingface.py
│   └── localmodel.py
├── embeddingmodels/
│   ├── embedding.py
│   └── huggingface_embedding.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 🛠️ Technologies Used

- Python
- LangChain
- Ollama
- Hugging Face
- Streamlit
- Text Embeddings
- Large Language Models (LLMs)

## ⚙️ Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/iampratikx/Gen-AI-Learning.git
cd Gen-AI-Learning
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file using `.env.example` as a template. Add your own API keys where required.

**Never upload your `.env` file or API keys to GitHub.**

### 5. Run an application

Navigate to the relevant project folder and run the appropriate Python script. For Streamlit applications, use:

```bash
streamlit run path/to/your_app.py
```

Replace the example path with the actual Streamlit entry-point file.

## 🎯 Purpose

The purpose of this repository is to strengthen my practical understanding of Generative AI, experiment with different models, and build small applications as part of my continuous learning journey.

## 🚧 Project Status

This is a learning and practice repository. Code and implementations may evolve as I explore new concepts and improve existing projects.

## 👨‍💻 Author

**Pratik Chavan**

- GitHub: https://github.com/iampratikx
- LinkedIn: https://www.linkedin.com/in/iampratikx
