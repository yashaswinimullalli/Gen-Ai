# Multimodal AI - Revision Notes

## What is Multimodal AI?

Multimodal AI is an AI system that can understand and process multiple types of data (modalities).

Instead of only text, it can work with:

* Text
* Images
* PDFs
* Audio
* Video

---

# What is a Modality?

A modality is a type of information.

Examples:

```text
Text   → Words
Image  → Pictures
PDF    → Documents
Audio  → Speech
Video  → Moving Visuals
```

Multimodal = Multiple Modalities

---

# Traditional LLM

```text
Text
↓
LLM
↓
Text
```

Example:

```text
Explain Python.
```

---

# Multimodal AI

```text
Text
Image
PDF
Audio
Video
↓
AI Model
↓
Response
```

Example:

```text
Describe this image.
```

---

# 1. Text Modality

Input:

```text
Explain OOP.
```

Output:

```text
OOP stands for Object-Oriented Programming...
```

---

# 2. Image Modality

Input:

```text
Image + Prompt
```

Example:

```text
Describe this image in detail.
```

Tasks:

* Image Description
* Object Detection
* Scene Understanding
* Image Analysis

---

# Image Analysis

Example:

```python
contents=[
    "Describe this image in detail.",
    image
]
```

Workflow:

```text
Image
↓
Gemini
↓
Description
```

---

# 3. OCR (Optical Character Recognition)

OCR means:

```text
Image
↓
Extract Text
```

Example:

Input Image:

```text
WELCOME TO NMIT
```

Output:

```text
WELCOME TO NMIT
```

Prompt:

```python
contents=[
    "Extract all text from this image.",
    image
]
```

Applications:

* Resume Parsing
* Notes Extraction
* Screenshot Analysis
* Invoice Processing

---

# 4. PDF Understanding

Input:

```text
PDF
```

Tasks:

* Summarization
* Question Answering
* MCQ Generation
* Information Extraction

Example:

```text
Resume PDF
↓
Extract Skills
↓
Generate Interview Questions
```

---

# 5. Audio Understanding

Input:

```text
Lecture Recording
```

Tasks:

* Speech Recognition
* Transcription
* Summarization
* Note Generation

Workflow:

```text
Audio
↓
Text
↓
Analysis
```

---

# 6. Video Understanding

Input:

```text
Interview Recording
```

Tasks:

* Video Summarization
* Event Detection
* Scene Understanding
* Question Answering

Workflow:

```text
Video
↓
Analysis
↓
Summary
```

---

# Contents Parameter in Gemini

Example:

```python
contents=[
    "Describe this image in detail.",
    image
]
```

Meaning:

```text
Prompt
+
Image
↓
Gemini
↓
Response
```

The same image can produce different outputs depending on the prompt.

Example:

```python
contents=[
    "Extract all text from this image.",
    image
]
```

or

```python
contents=[
    "Describe this image.",
    image
]
```

---

# Multimodal AI vs RAG

## Multimodal AI

Focus:

```text
Different Data Types
```

Example:

```text
Image
↓
Understand Image
```

---

## RAG

Focus:

```text
External Knowledge Retrieval
```

Example:

```text
PDF
↓
Retrieve Information
↓
Answer Questions
```

---

# Airah AI Use Cases

```text
Resume Screenshot
↓
OCR

Resume PDF
↓
Analysis

Interview Audio
↓
Speech Analysis

Portfolio Images
↓
Project Understanding
```

---

# Key Takeaways

✅ Multimodal AI works with multiple data types

✅ Modalities include Text, Images, PDFs, Audio, and Video

✅ Image Analysis describes image content

✅ OCR extracts text from images

✅ PDF Understanding analyzes documents

✅ Audio Understanding processes speech

✅ Video Understanding analyzes videos

✅ Prompt + Image = Different Outputs

---

# Interview Definition

What is Multimodal AI?

Multimodal AI is an AI system that can understand, process, and reason over multiple types of data such as text, images, audio, video, and documents to generate meaningful outputs.
