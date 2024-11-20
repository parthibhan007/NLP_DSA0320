import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

# Define the grammar with subject-verb agreement rules
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N_S | Det N_P
    VP -> V_S | V_P
    Det -> 'the' | 'a'
    N_S -> 'dog' | 'cat' | 'child'
    N_P -> 'dogs' | 'cats' | 'children'
    V_S -> 'runs' | 'barks' | 'plays'
    V_P -> 'run' | 'bark' | 'play'
""")

# Function to check agreement in sentences
def check_agreement(sentence, grammar):
    parser = RecursiveDescentParser(grammar)
    tokens = sentence.split()
    valid = False
    for tree in parser.parse(tokens):
        valid = True
        break
    return valid

# Test sentences
sentences = [
    "the dog runs",        # Valid
    "the dogs run",        # Valid
    "the cat barks",       # Valid
    "the cats bark",       # Valid
    "the dog run",         # Invalid
    "the dogs barks",      # Invalid
    "the children play",   # Valid
    "a child plays",       # Valid
    "a child play",        # Invalid
]

# Check sentences and print results
print("Sentence Validity Check:")
for sentence in sentences:
    if check_agreement(sentence, grammar):
        print(f"'{sentence}' is valid.")
    else:
        print(f"'{sentence}' is invalid.")
