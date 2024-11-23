from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Example documents
documents = [
    "The sky is blue and beautiful.",
    "Love this blue and bright sky!",
    "The quick brown fox jumps over the lazy dog.",
    "A king's breakfast has sausages, ham, bacon, and eggs.",
    "Blue birds are flying in the sky."
]

# Query
query = "blue sky"

# TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(documents + [query])

# Cosine similarity
cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

# Rank documents
ranked_docs = sorted(enumerate(cosine_similarities), key=lambda x: x[1], reverse=True)

print("Document Rankings:")
for idx, score in ranked_docs:
    print(f"Document {idx + 1}: {score:.4f}")
