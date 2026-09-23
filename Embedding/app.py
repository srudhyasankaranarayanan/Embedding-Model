from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Predefined sentences
sentences = [
    "I love learning Python",
    "Machine learning is interesting",
    "I enjoy programming",
    "The weather is very hot today",
    "I like playing music"
]

# List to store embeddings
sentence_embedding = []

# Get two sentences from the user
sentence1 = input("Enter sentence 1: ")
sentence2 = input("Enter sentence 2: ")

# Add user sentences to the list
sentences.append(sentence1)
sentences.append(sentence2)

# Generate embeddings
for sentence in sentences:

    embedding = model.encode(sentence)

    sentence_embedding.append(embedding)

# Display embeddings
print("\n========== EMBEDDINGS ==========")

for i in range(len(sentences)):

    print("\nSentence:", sentences[i])
    print("Embedding:", sentence_embedding[i])
    print("Dimension:", len(sentence_embedding[i]))

# Get embeddings of user sentences
embedding1 = sentence_embedding[-2]
embedding2 = sentence_embedding[-1]

# Calculate cosine similarity
similarity = cosine_similarity(
    [embedding1],
    [embedding2]
)

# Display similarity score
print("\n========== SIMILARITY ==========")

print("\nSentence 1:", sentence1)
print("Sentence 2:", sentence2)

print("\nSimilarity Score:")
print(similarity[0][0])