# Embedding Models

## About the Project

This project is about **Embedding Models**. I used a Sentence Transformer model to convert sentences into numerical values called **embeddings**.

I also used **cosine similarity** to compare two sentences and find how similar their meanings are.

---

## What I Learned

Through this project, I learned:

* What embeddings are
* How text is converted into numerical vectors
* How to generate embeddings using Sentence Transformers
* What embedding dimensions mean
* How to compare two embeddings
* How cosine similarity works

---

## Model Used

I used:

```text
all-MiniLM-L6-v2
```

This model converts each sentence into a **384-dimensional embedding**.

For example:

```text
"I love coding"
      ↓
Embedding Model
      ↓
Numerical Vector
```

---

## How My Program Works

First, I load the Sentence Transformer model.

Then I give some sentences as input and also enter two sentences manually.

The program uses:

```python
model.encode(sentence)
```

to convert every sentence into an embedding.

The embeddings are stored in a list using a `for` loop.

After generating the embeddings, the program uses **cosine similarity** to compare the embeddings of the two sentences entered by the user.

---

## Working Flow

```text
Enter Sentences
      ↓
Load Embedding Model
      ↓
Convert Sentences into Embeddings
      ↓
Store Embeddings
      ↓
Get Embeddings of Two Sentences
      ↓
Calculate Cosine Similarity
      ↓
Display Similarity Score
```

---

## Example

If I enter:

```text
Sentence 1: I love coding

Sentence 2: I enjoy programming
```

The model creates an embedding for both sentences.

Then cosine similarity compares the two embeddings and gives a similarity score.

A higher score generally means that the two sentence embeddings are more similar.

---

## Key Concepts

### Embedding
A numerical representation of text that captures its meaning.

### Embedding Dimension
The number of values present in an embedding vector. In this project, each embedding has 384 values.

### Cosine Similarity
A method used to compare two embedding vectors and measure their semantic similarity.

## Technologies Used

* Python
* Sentence Transformers
* Scikit-learn

---

## Libraries Required

The `requirements.txt` file contains:

```text
sentence-transformers
scikit-learn
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## How to Run

First install the required libraries:

```bash
pip install -r requirements.txt
```

Then run the Python file:

```bash
python embedding.py
```

Enter two sentences when the program asks for them.

---

## Output

The program displays:

* The sentences
* Their embedding vectors
* Embedding dimension
* The similarity score between the two entered sentences

---

## Project Structure

```
Embedding-Models/
│
├── embedding.py
├── requirements.txt
├── README.md
└── output.png
```

## Applications

Embedding models can be used for:

* Semantic search
* Finding similar sentences
* Document similarity
* Question matching
* Recommendation systems
* RAG applications

---

## Conclusion

From this project, I understood how an **Embedding Model converts text into numerical vectors**. I also learned that these vectors can be compared using **cosine similarity** to find the semantic similarity between sentences.

## Author

**Srudhya Sankaranarayanan**
