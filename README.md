# PDF-Chatbot-using-OPENAI

## Introduction

The PDF Based Chatbot is an interactive application built with Streamlit that leverages the power of LangChain and OpenAI's language model. The chatbot allows users to extract information and perform natural language queries on PDF documents. It utilizes LangChain's capabilities for processing natural language instructions and OpenAI's language model for understanding user queries.

## Architecture of chatbot

![Screenshot 2023-08-03 at 00-06-29 PDF Based Chatbot Using Streamlit (🦜️🔗LangChain ⚙OpenAI)](https://github.com/MadhavJain0119/PDF-Chatbot-using-OPENAI/assets/82666405/31a21778-98a0-4831-bd73-e7ce12a4b011)

## Features

- **PDF Document Upload:** Users can upload PDF documents containing information they want to extract or query.
- **Text Extraction:** The chatbot automatically extracts text content from the uploaded PDF documents.
- **Natural Language Queries:** Users can interact with the chatbot using natural language to perform searches and ask questions about the document content.
- **LangChain Integration:** LangChain is utilized to process user instructions and convert them into actionable tasks for the chatbot.
- **OpenAI Language Model:** OpenAI's powerful language model is used to comprehend user queries and generate relevant responses.
- **Interactive Interface:** The user-friendly Streamlit interface allows users to easily interact with the chatbot.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/pdf-chatbot.git
cd pdf-chatbot
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:

``` bash
streamlit run app.py
``` 

- The app will be available in your browser at http://localhost:8501.

- Upload a PDF document and start interacting with the chatbot using natural language.

## Dependencies

- Streamlit
- LangChain
- OpenAI GPT-3 Language Model
- Other dependencies are listed in the requirements.txt file.
