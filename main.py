from data.corpus import corpus
from src.train_model import train_model
from src.vector_store import create_vector_db
from src.similarity_search import get_top_k_similar
from src.visualize import plot_embeddings

def main():
    model = train_model(corpus)
    vector_db = create_vector_db(model)
    
    query = "bank"
    results = get_top_k_similar(model, vector_db, query)
    
    print(f"\nQuery: {query}")
    print("Top 4 similar words:")
    
    for word, score in results:
        print(word)
    
    plot_embeddings(vector_db)

if __name__ == "__main__":
    main()
