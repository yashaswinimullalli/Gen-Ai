# Prompt Engineering 

## What is Prompt Engineering?

Prompt Engineering is the process of designing effective prompts to get better responses from Large Language Models (LLMs).

### Goal

```text
Better Prompt
+
Same Model
=
Better Output
```

---

# Prompt Formula

```text
ROLE
+
TASK
+
CONTEXT
+
CONSTRAINTS
+
OUTPUT FORMAT
```

Example:

```text
You are a technical interviewer.

Generate 5 Python interview questions for a fresher.

Constraints:
- Beginner level
- Focus on fundamentals

Output Format:
Question | Difficulty | Expected Answer
```

---

# 1. Zero-Shot Prompting

### Definition

Giving a task without examples.

### Example

```text
Explain OOP to a first-year engineering student.
```

### Use Cases

* Summarization
* Explanation
* Question Answering

---

# 2. Few-Shot Prompting

### Definition

Providing examples before asking the task.

### Example

```text
Question: What is Python?
Difficulty: Easy

Question: Explain Dynamic Programming.
Difficulty:
```

### Use Cases

* Classification
* Formatting
* Pattern Learning

---

# 3. Role Prompting

### Definition

Assigning a role to the model.

### Examples

```text
You are a professor.
```

```text
You are a software engineer.
```

```text
You are a technical interviewer.
```

### Benefit

Changes the style and expertise of the response.

---

# 4. Structured Prompting

### Definition

Specify the output format.

### Example

```text
Explain DBMS in the following format:

Definition:
Advantages:
Disadvantages:
Applications:
```

### Benefit

Produces organized and consistent output.

---

# 5. Constraints

### Definition

Setting rules and limitations.

### Example

```text
Explain OOP.

Constraints:
- Maximum 100 words
- Use simple language
- Give one example
```

### Benefit

Controls response quality and length.

---

# 6. Chain of Thought (CoT)

### Definition

Ask the model to reason step-by-step.

### Example

```text
Think step-by-step and explain your reasoning.
```

### Use Cases

* Math Problems
* Logic
* Coding
* Interview Evaluation

---

# Best Practices

✅ Be specific

✅ Give context

✅ Define a role

✅ Specify output format

✅ Add constraints

✅ Use examples when needed

---

# Key Takeaway

Prompt Engineering is not about asking better questions.

It is about giving the model:

```text
Role
+
Task
+
Context
+
Constraints
+
Format
```

to obtain reliable and high-quality outputs.
