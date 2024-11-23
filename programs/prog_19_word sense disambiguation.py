from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def lesk_algorithm(word, sentence):
    words = set(word_tokenize(sentence))
    best_sense = None
    max_overlap = 0
    for sense in wn.synsets(word):
        definition = sense.definition()
        examples = ' '.join(sense.examples())
        signature = set(word_tokenize(definition + ' ' + examples))
        signature -= set(stopwords.words('english'))
        overlap = len(signature.intersection(words))
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense
    return best_sense

# Input text
sentence = "He went to the bank to withdraw money."
word = "bank"
sense = lesk_algorithm(word, sentence)

if sense:
    print(f"Best sense for '{word}': {sense.name()} - {sense.definition()}")
