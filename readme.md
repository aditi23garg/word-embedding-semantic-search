# 🧠 Word Embedding & Semantic Search Project

## 📌 Overview

This project demonstrates how to build a **semantic search system** using **Word2Vec embeddings**. It converts words into vectors, stores them in a vector database, and retrieves the most similar words based on cosine similarity.

Additionally, it visualizes embeddings in a 2D space using PCA.

---

## 🎯 Objectives

* Convert text corpus into word embeddings
* Store embeddings in a vector database
* Perform similarity search on query words
* Visualize embeddings in 2D space

---

## 📂 Project Structure

```
word-embedding-semantic-search/
│
├── data/                  # Input corpus
├── src/                   # Core modules
├── outputs/               # Visualization output
├── main.py                # Entry point
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── .gitignore             # Ignore unnecessary files
```

---

## 📊 Dataset

The corpus contains sentences with ambiguous words like **"bank"**, used in both financial and river contexts.

Example:

```
bank loan credit finance money
river bank water flow stream
```

---

## ⚙️ Technologies Used

* Python
* Gensim (Word2Vec)
* Scikit-learn (Cosine Similarity, PCA)
* Matplotlib (Visualization)
* NumPy

---

## 🚀 How It Works

### 1️⃣ Train Word Embeddings

* Tokenize corpus
* Train Word2Vec model

### 2️⃣ Store in Vector DB

* Store word → vector mapping

### 3️⃣ Similarity Search

* Input query word
* Compute cosine similarity
* Retrieve top 4 similar words

### 4️⃣ Visualization

* Reduce dimensions using PCA
* Plot embeddings in 2D

---

## ▶️ How to Run

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/word-embedding-semantic-search.git
cd word-embedding-semantic-search
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Project

```bash
python main.py
```

---

## 📌 Example Output

### Input:

```
Query: bank
```

### Output:

```
Top 4 similar words:
finance
loan
money
credit
```

---

## 📈 Output Visualization

* Embeddings plotted in 2D space
* Words with similar meanings appear closer

---

## 💡 Key Concepts Used

* Word Embeddings (Word2Vec)
* Cosine Similarity
* Vector Databases (Simulated)
* Dimensionality Reduction (PCA)
* Semantic Search

---

## 🔥 Future Enhancements

* Use **BERT embeddings**
* Integrate **FAISS or Pinecone**
* Improve visualization with **t-SNE / UMAP**
* Build a web interface using Flask or Streamlit
