import spacy

# Load the SpaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_noun_phrases(sentence):
    doc = nlp(sentence)
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    return noun_phrases

sentence = "The intelligent student quickly solved the challenging math problem."
noun_phrases = extract_noun_phrases(sentence)
print("Noun Phrases:", noun_phrases)
