import spacy

# Load the SpaCy language model
nlp = spacy.load("en_core_web_md")

# Input text
text = "Apple Inc. is planning to open a new office in San Francisco by next year."

# Process the text
doc = nlp(text)

# Extract named entities
print("Named Entities, their labels, and positions:")
for ent in doc.ents:
    print(f"{ent.text} ({ent.label_}) [{ent.start_char}, {ent.end_char}]")
