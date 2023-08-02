import streamlit as st
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os
from altair.vegalite.v4.api import Chart
import altair as alt

def main():
    st.title("PDF Question Answering")
    file = st.file_uploader("Upload a PDF file", type="pdf")

    if file is not None:
        st.write("PDF file uploaded successfully.")

        pdf_reader = PdfReader(file)
        raw_data = ''
        for i, page in enumerate(pdf_reader.pages):
            data = page.extract_text()
            if data:
                raw_data += data

        data_split = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        datas = data_split.split_text(raw_data)

        import os
        import openai
        os.environ["OPENAI_API_KEY"] = "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"
        openai.api_key = "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"

        embeddings = OpenAIEmbeddings(openai_api_key= "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")
        docsearch = FAISS.from_texts(datas, embeddings)

        chain = load_qa_chain(OpenAI(model="davinci"), chain_type="stuff")

        query = st.text_input("Enter your question:")
        if st.button("Get Answer"):
            response = docsearch.similarity_search(query)
            answer = chain.run(input_documents=response, question=query)
            st.write(f"Answer: {answer}")


if __name__ == '__main__':
    main()
