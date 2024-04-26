# Semantic-Search-Engine-For-Movie-Subtitles

This project involves creating a semantic search engine specifically designed for retrieving subtitle content based on user queries. By leveraging advanced natural language processing (NLP) techniques, including BERT-based embeddings, the search engine aims to improve the relevance and accuracy of search results.

The project consists of two main phases: data ingestion and retrieval. In the first phase, the subtitle documents are read from a given database, preprocessed to remove noise and irrelevant data, and then divided into manageable chunks to avoid information loss during embedding. The embeddings are generated using a BERT-based model, and the resulting text vectors are stored in a ChromaDB database for efficient retrieval.

In the second phase, the search engine takes user queries, preprocesses them, and converts them into embeddings. Using cosine similarity, it calculates the similarity scores between the query embeddings and the stored embeddings to find the most relevant subtitle content. The retrieved results are sorted and presented to the user, providing a seamless search experience.

Overall, this project demonstrates the effectiveness of semantic search and machine learning techniques in improving the accuracy and efficiency of subtitle retrieval, offering a scalable and high-performance solution for advanced information retrieval tasks.

![image](https://github.com/Samyank-m18/Semantic-Search-Engine-For-Movie-Subtitles/assets/115860318/e460d189-e336-4f0d-8b9e-95e0cbf44f45)
