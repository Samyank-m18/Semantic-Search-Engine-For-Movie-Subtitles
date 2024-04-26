import re
import chromadb
from sentence_transformers import SentenceTransformer
import streamlit as st
from chromadb.utils import embedding_functions


chroma_client_1 = chromadb.PersistentClient(path="my_chromadb1")

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")


collection_1 = chroma_client_1.get_or_create_collection(name="my_collection_1", embedding_function=sentence_transformer_ef,metadata ={"hnsw:space":"cosine"})







def clean_data(data): # data is the query text

    # removing timestamps
    data = re.sub("\d{2}:\d{2}:\d{2},\d{3}\s-->\s\d{2}:\d{2}:\d{2},\d{3}"," ",  data)

    # removing index no. of dialogues
    data = re.sub(r'\n?\d+\r', "", data)

    # removing escape sequences like \n \r
    data = re.sub('\r|\n', "", data)

    # removing <i> and </i>
    data = re.sub('<i>|</i>', "", data)
    # removing links
    data = re.sub("(?:www\.)osdb\.link\/[\w\d]+|www\.OpenSubtitles\.org|osdb\.link\/ext|api\.OpenSubtitles\.org|OpenSubtitles\.com", " ",data)

    # Converting to lower case
    data = data.lower()

    # return
    return data



# def clean_text(text):
#     cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
#     cleaned_text = re.sub(r'[^\x00-\x7F]+', '', cleaned_text)
#     cleaned_text = re.sub(r'\d{2}:\d{2}:\d{2}\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', cleaned_text)
#     cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
#     cleaned_text = cleaned_text.lower().strip()
    
#     return cleaned_text


st.header("Movie Subtitle Search Engine")
search_query = st.text_area("Enter a Dialogue from movie to Search")

if st.button("Search") == True :
    st.subheader("Relevant Subtitle Files")
    search_query = clean_data(search_query)

    results = collection_1.query(
    query_texts=search_query,
    n_results=10,
    include=['documents', 'distances', 'metadatas']
    )

    # Ensure we're accessing the correct keys and indices
    documents = results['documents'][0]  # Get the first list of documents
    metadatas = results['metadatas'][0]  # Get the first list of metadatas

    for document, metadata in zip(documents, metadatas):
        item_id = metadata['item_id']  # Extract 'item_id' from the metadata
        st.markdown(f"- {document}, (https://www.opensubtitles.org/en/subtitles/{item_id})") 