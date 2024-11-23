import spacy
import neuralcoref

# Load SpaCy with neural coref
nlp = spacy.load("en_core_web_sm")
neuralcoref.add_to_pipe(nlp)

def resolve_references(text):
    doc = nlp(text)
    return doc._.coref_resolved

text = "John said he would help Mary with her project."
resolved_text = resolve_references(text)
print("Resolved Text:", resolved_text)
