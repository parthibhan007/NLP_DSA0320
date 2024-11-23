def evaluate_coherence(text):
    sentences = text.split(". ")
    overlap_count = 0
    for i in range(len(sentences) - 1):
        words_current = set(sentences[i].lower().split())
        words_next = set(sentences[i + 1].lower().split())
        overlap_count += len(words_current & words_next)

    coherence_score = overlap_count / (len(sentences) - 1)
    return coherence_score

text = "The cat is on the mat. The mat is very soft. Soft materials are comfortable."
coherence_score = evaluate_coherence(text)
print(f"Coherence Score: {coherence_score:.2f}")
