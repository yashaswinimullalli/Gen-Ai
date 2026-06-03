# GenAI Engineering

A hands-on learning repository documenting my journey from LLM fundamentals to advanced Generative AI concepts.

This repository contains notes, experiments, and mini-projects covering Prompt Engineering, Retrieval-Augmented Generation (RAG), and Multimodal AI using Google's Gemini API and Python.

---

## Learning Roadmap

```text
GenAI Engineering
│
├── LLM Fundamentals          ✅
├── Prompt Engineering        ✅
├── RAG Fundamentals          ✅
├── Multimodal AI             ✅
├── AI Agents                 ⏳
├── Evaluation                ⏳
├── Production Systems        ⏳
└── Fine-Tuning               ⏳
```

---

## Repository Structure

```text
GenAI-Engineering/
│
├── Prompt-Engineering/
│   └── prompt_engineering_notes.md
│
├── RAG/
│   ├── mini_rag.py
│   └── rag_revision_notes.md
│
├── Multimodal-AI/
│   ├── image_analyzer.py
│   └── multimodal_ai_notes.md
│
└── README.md
```

---

## Topics Covered

### 1. Prompt Engineering

Learned techniques:

* Zero-Shot Prompting
* Few-Shot Prompting
* Role Prompting
* Constraints
* Structured Outputs
* Chain of Thought (CoT)

Key Formula:

```text
Role
+
Task
+
Context
+
Constraints
+
Output Format
```

---

### 2. Retrieval-Augmented Generation (RAG)

Learned concepts:

* Retrieval
* Augmentation
* Generation
* Chunking
* Embeddings
* Semantic Search
* Vector Databases
* Retrieval Pipeline

Built:

* Mini RAG System

RAG Pipeline:

```text
Document
↓
Chunking
↓
Embeddings
↓
Vector Database
↓
Retrieve Relevant Chunks
↓
LLM
↓
Answer
```

---

### 3. Multimodal AI

Learned concepts:

* Image Understanding
* OCR (Optical Character Recognition)
* PDF Understanding
* Audio Understanding
* Video Understanding

Built:

* Image Analyzer using Gemini Vision

Multimodal Inputs:

```text
Text
Images
PDFs
Audio
Video
```

---

## Technologies Used

* Python
* Google Gemini API
* python-dotenv
* Pillow (PIL)

---

## Setup

### Clone Repository

```bash
git clone <repository-url>
cd GenAI-Engineering
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install google-genai python-dotenv pillow
```

### Configure API Key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Learning Outcomes

By completing these modules, I learned:

* How to interact with LLMs programmatically
* How Prompt Engineering improves outputs
* How RAG enables AI to use external knowledge
* How Embeddings and Vector Databases work
* How Multimodal AI processes images and documents
* Foundations required for building production-grade AI applications

---

## Future Work

* AI Agents
* Evaluation Frameworks
* Production AI Systems
* Fine-Tuning
* Airah AI (AI-Powered Career & Interview Preparation Platform)

---

## Author

Yashaswini Mullalli

Computer Science Student | Generative AI Learner | Future AI Engineer 🚀
