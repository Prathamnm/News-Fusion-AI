
#  **News-Fusion-AI**

### *Autonomous RAG-Powered News Intelligence System*

News-Fusion-AI is an **end-to-end autonomous news intelligence framework** that collects, cleans, embeds, indexes, and retrieves news across multiple global sources using **LangChain**, **FAISS**, **Sentence-Transformers**, and **RAG architecture**.
It transforms raw news into a **query-ready knowledge base**, enabling users to ask natural-language questions and receive **context-aware, source-backed answers**.

> Built with the power of **LangChain**, **Retrieval-Augmented Generation**, and **Antigravity (Google)** for accelerated document processing.

---

##  **Purpose**

Traditional news platforms scatter information across multiple sources. News-Fusion-AI solves this by:

* Aggregating news from trusted global sources
* Structuring & cleaning raw news articles
* Converting them into embeddings for deep semantic understanding
* Providing intelligent Q&A capability over the entire dataset

The goal is to create a **fully automated news pipeline** that behaves like an AI research assistant for real-time information.

---

#  **Core Features**

### **✔ Multi-Source News Collection**

Supports scraping news from:

* BBC
* CNN
* Google News
* Al Jazeera
* India Today
* Financial Express
* Twitter *(with custom scraper)*

---

### **✔ Intelligent Preprocessing Layer**

The preprocessing system:

* Removes HTML / noise
* Standardizes text
* Splits into optimized chunks
* Generates clean, structured datasets

---

### **✔ RAG Architecture (Retrieval-Augmented Generation)**

A complete RAG pipeline consisting of:

* Semantic embeddings via **MiniLM-L6-V2**
* Vector storage in **FAISS**
* A **LangChain retriever** for relevant document search
* A response-generator LLM with contextual grounding

This makes answers:
**accurate**, **source-aware**, and **hallucination-resistant**.

---

### ✔ **Autonomous Pipeline Workflow**

News-Fusion-AI can run as a scheduled process that:

1. Collects latest news
2. Processes & chunks data
3. Generates embeddings
4. Stores to FAISS DB
5. Enables intelligent real-time querying

---

#  **Architecture Overview**

```
 Collectors/
│
├── bbc_news.py
├── cnn_news.py
├── google_news.py
├── aljazeera_news.py
└── twitter_scraper.py
```

```
 Preprocess/
│
├── cleaner.py
└── prepare_docs.py
```

```
 RAG/
│
├── create_vectorstore.py
├── retriever.py
└── rag_chain.py
```

```
 main.py   # Runs the AI answering system
 data/vectorstore/  # FAISS DB
```

---

#  **Workflow**

### **1️⃣ Data Collection**

News is pulled from multiple agencies using custom API & scraper scripts.

### **2️⃣ Preprocessing**

Cleaning, normalizing, chunking & preparing a document corpus.

### **3️⃣ Embedding Generation**

Using Sentence-Transformers (MiniLM):

* Converts each chunk to a 384-D embedding
* Stores them efficiently in FAISS

### **4️⃣ Semantic Retrieval**

User query → Vector search → Top relevant chunks extracted.

### **5️⃣ Generative Answering**

LLM answers using retrieved evidence, ensuring factuality.

---

#  **Tech Stack**

### **AI + NLP**

* LangChain
* Sentence-Transformers MiniLM
* FAISS Vector DB
* RAG Pipeline
* Antigravity

### **Backend**

* Python
* Requests / BeautifulSoup
* OS / FS automation

### **Optionally**

* Streamlit / React (Dashboard)

---

# 🔧 **Installation & Setup**

### **1. Clone the repository**

```bash
git clone https://github.com/Prathamnm/News-Fusion-AI
cd News-Fusion-AI
```

---

## **2. Install Dependencies**

Make sure you have Python 3.10+ installed.

```bash
pip install -r requirements.txt
```

---

#  **3. Generate Your Hugging Face API Key**

The project uses **Hugging Face Inference API** for embeddings (Sentence Transformers).

**Steps to generate the key:**

1. Go to: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Click **"New Token"**
3. Select type → **Read**
4. Copy the generated API key

---

#  **4. Create `.env` File**

Inside your project root folder, create a `.env` file:

```
HF_TOKEN=your_huggingface_api_key_here
```


---

#  **5. Run the RAG Pipeline**

The entire pipeline (collection → preprocessing → embedding → retrieval) can be tested via the `rag_test.py` file.

Run:

```bash
python rag_test.py
```

This script will:
✔ Load FAISS vectorstore
✔ Load embeddings
✔ Run the retrieval chain
✔ Ask you to enter news-related questions
✔ Return an AI-generated answer grounded in news sources

---

#  **Optional: Regenerate Vectorstore**

If you want to refresh embeddings after collecting new news:

```bash
python rag/create_vectorstore.py
```

---

#  **Use Cases**

###  For Researchers

Query real-time global events with context.

###  For Journalists

Summarize multi-source news instantly.

###  For Students & Analysts

Understand events through fact-grounded AI.

---

#  **Future Enhancements**

* 🌐 Add more news categories
* 📊 Real-time monitoring dashboard
* 🧩 Plugin interface for new sources
* ☁️ Cloud vector DB (Pinecone / Qdrant)

---

#  **Acknowledgements**

* LangChain
* Sentence-Transformers
* HuggingFace
* FAISS
* Google Antigravity
* All news sources used

---



