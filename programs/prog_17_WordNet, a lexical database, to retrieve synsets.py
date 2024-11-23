from nltk.corpus import wordnet as wn

# Word to explore
word = "bank"

# Retrieve synsets
synsets = wn.synsets(word)

print(f"Synsets for '{word}':")
for synset in synsets:
    print(f"{synset.name()}: {synset.definition()}")

# Explore a specific synset
if synsets:
    synset = synsets[0]
    print("\nExamples and lemmas for first synset:")
    print(f"Examples: {synset.examples()}")
    print(f"Lemmas: {[lemma.name() for lemma in synset.lemmas()]}")
