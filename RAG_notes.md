# RAG (Retrieval-Augmented Generation) 

## What is RAG?

RAG (Retrieval-Augmented Generation) is a technique that allows an LLM to use external knowledge while generating responses.

### Formula

```text
Retrieval + Augmentation + Generation
```

---

# Why Do We Need RAG?

Problem:

LLMs only know information from their training data.

They do not know:

* Your Resume
* Your Notes
* Company Documents
* PDFs
* Private Data

Solution:

```text
Document
↓
Retrieve Relevant Information
↓
Add to Prompt
↓
LLM Generates Answer
```

---

# Components of RAG

## 1. Retrieval

Find relevant information from documents.

Example:

```text
Question:
Generate interview questions.

Retrieved:
Skills: Python, SQL
Projects: RoadSathi
```

---

## 2. Augmentation

Add retrieved information to the prompt.

Example:

```text
Candidate Skills:
Python
SQL

Generate interview questions.
```

---

## 3. Generation

The LLM generates the final answer using the retrieved context.

---

# RAG vs Normal Chatbot

## Normal Chatbot

```text
Question
↓
LLM
↓
Answer
```

Uses only model knowledge.

---

## RAG Chatbot

```text
Question
↓
Retrieve Information
↓
LLM
↓
Answer
```

Uses external knowledge.

---

# Chunking

Large documents are split into smaller pieces called chunks.

Example:

```text
Resume
↓
Chunk 1 → Personal Details
Chunk 2 → Skills
Chunk 3 → Projects
Chunk 4 → Education
```

Benefits:

* Faster retrieval
* Better relevance
* Lower cost

---

# Embeddings

Embeddings convert text into numerical vectors.

Example:

```text
Python Developer
↓
[0.24, -0.81, 0.62, ...]
```

Purpose:

* Capture meaning
* Enable semantic search

---

# Semantic Search

Searches based on meaning rather than exact words.

Example:

```text
Query:
Python Engineer
```

Can retrieve:

```text
Python Developer
Backend Python Developer
```

because meanings are similar.

---

# Vector Database

Stores embeddings for fast retrieval.

Popular Vector Databases:

* ChromaDB
* FAISS
* Pinecone
* Weaviate

Purpose:

```text
Store Meaning
Not Just Text
```

---

# Complete RAG Pipeline

```text
PDF
↓
Chunking
↓
Embeddings
↓
Vector Database
↓
User Question
↓
Question Embedding
↓
Similarity Search
↓
Retrieve Chunks
↓
LLM
↓
Answer
```

---

# Real-World Applications

## Resume Analyzer

```text
Resume
↓
Extract Skills
↓
Generate Questions
```

---

## Study Assistant

```text
Notes PDF
↓
Ask Questions
↓
Get Answers
```

---

## Company Knowledge Bot

```text
Company Documents
↓
Employee Questions
↓
Accurate Responses
```

---

# Limitations of RAG

## Bad Chunking

Wrong document splitting can lead to poor retrieval.

---

## Bad Embeddings

Relevant information may not be found.

---

## Hallucinations

LLMs can still generate incorrect information.

---

# Interview Definition

What is RAG?

RAG (Retrieval-Augmented Generation) is a technique where relevant information is retrieved from external knowledge sources, added to the prompt, and then used by an LLM to generate accurate and context-aware responses.

---

# Key Takeaways

✅ RAG allows LLMs to use external knowledge

✅ Chunking splits large documents into smaller pieces

✅ Embeddings convert text into vectors

✅ Semantic Search retrieves information based on meaning

✅ Vector Databases store embeddings

✅ RAG powers PDF Chatbots, Resume Analyzers, and Knowledge Assistants
