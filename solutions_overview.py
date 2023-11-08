import streamlit as st


st.set_page_config(page_title="Solutions Overview", layout="wide")
css = '''
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            # padding-left: 5rem;
            # padding-right: 5rem;
        }                
    </style>
'''
st.write(css, unsafe_allow_html=True)
st.header("Demo Solutions overview")
st.write("This page provides an overview of the solutions used by the demos listed in the sidebar.")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Question Answering", "Chatbot", "Text Search", "Code Translation", "RAG - Documents", "RAG - Web Search"])
with tab1:
    # FM QA using Amazon Bedrock
    st.subheader("Question Answering with Amazon Bedrock FMs")
    st.markdown("""
    This demo shows you an interaction with an FM hosted by Amazon Bedrock, with questions or instructions. This demo solution uses:
    - Streamlit for the web interface
    - AWS SDK for python (Boto3) for API access to FMs via API calls to Amazon Bedrock

    """)
    st.image('QA-FM.png', caption="FM Question Answering using Amazon Bedrock", width=650)
with tab2:
    # FM chat using Amazon Bedrock
    st.subheader("Chat with Amazon Bedrock FMs")
    st.markdown("""
    This demo shows you how to chat with an FM. A chat stores your **conversation history** and provides it as context to the FM along with your question or instruction. This demo solution uses:
    - Streamlit for the web interface
    - AWS SDK for python (Boto3) for API access to FMs via API calls to Amazon Bedrock

    """)
    st.image('CHAT-FM.png', caption="FM chat using Amazon Bedrock", width=650)  
with tab3:  
    # Text Search
    st.subheader("Text Search")
    st.markdown("""
    This demo shows the results of searching for information from text with similarity search and a contextual query to an FM:  
    - **Similarity search:** Split text into sentences, convert sentences and query into embeddings, store embeddings in a vector datastore and find sentences whose embeddings are closest to that of the query (most similar).  A similarity search considers the semantics and context of the query based on closeness of vectors or embeddings.
    - **Contextual search:** Create a prompt with the query and the entire text as context to generate a response from an FM (hosted on Amazon Bedrock).
                
    """)
    st.markdown("""
    This demo solution uses:
    - Streamlit for the web interface
    - AWS SDK for python (Boto3) for API access to FMs via Amazon Bedrock
    - LangChain library for using FMs and vector datastores
    - The Amazon Titan Embeddings G1 - Text FM for generating embeddings
    - The FAISS vector datastore for storing, indexing and searching embeddings
    - The Anthropic Claude v2 FM for genertating answers to natural language queries

    """)
    st.image('Text-Search.png', caption="Text Search - Similarity/Contextual", width=650)
with tab4:
    # Code Translation using Amazon Bedrock
    st.subheader("Code Translation with Amazon Bedrock FMs")
    st.markdown("""
    This demo shows you how to translate code between programming languages using Amazon Bedrock. Anthropic and Cohere FMs have been optimized for code and used for this demo. This demo solution uses:
    - Streamlit for the web interface
    - AWS SDK for python (Boto3) for API access to FMs via API calls to Amazon Bedrock
                
    """)
    st.image('Code-Translation.png', caption="Code Translation using Amazon Bedrock", width=650)
with tab5:
    # RAG - PDF Documents
    st.subheader("Retrieval Augmented Generation (RAG) - PDF Documents")
    st.markdown("This demo shows you how to retrieve information from PDF documents using the RAG technique with FMs. When you upload a PDF document, it is split into chunks, the chunks are conveterd into embeddings and stored in a vector datastore. When you ask a question or send an instruction, your question/instruction is converted into embeddings and used for a similarity search to **retrieve** similar chunks of information from the vector datastore. The information retrieved is then used as context to **augment** a prompt to an FM to enable it **generate** an appropriate response.")
    st.markdown("""
    This demo solution uses:
    - Streamlit for the web interface
    - AWS SDK for python (Boto3) for API access to FMs via Amazon Bedrock
    - LangChain library for using FMs and vector datastores
    - The Amazon Titan Embeddings G1 - Text FM for generating embeddings
    - The FAISS vector datastore for storing, indexing and searching embeddings
    - Text-to-Text Bedrock FMs for generating answers to natural language queries

    """)
    st.image('RAG-Documents.png', caption="Retrieval Augmented Generation - Text Documents", width=650)
with tab6:
    # RAG - WWW
    st.subheader("Retrieval Augmented Generation (RAG) - Web Search")
    st.markdown("""
    This demo shows you how to retrieve information from the WWW using the RAG technique with FMs. When you ask a question or send an instruction, your question/instruction is used for a web search (using DuckDuckGo) to **retrieve** relevant information from the web. The information retrieved is then used as context to **augment** a prompt to an FM to enable it **generate** an appropriate response.
    This demo solution uses:
    - Streamlit for the web interface
    - AWS SDK for python (Boto3) for API access to FMs via API calls to Amazon Bedrock
    - LangChain library for DuckDuckGoSearch
                
    """)
    st.image('RAG-WWW.png', caption="Retrieval Augmented Generation - WWW", width=650)