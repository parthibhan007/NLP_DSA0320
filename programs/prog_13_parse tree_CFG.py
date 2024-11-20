import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

# Define the grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det Adj N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'man' | 'telescope'
    Adj -> 'big' | 'small'
    V -> 'saw' | 'likes'
""")

# Define the input sentence
sentence = "the big dog saw a cat".split()

# Create a parser using the grammar
parser = RecursiveDescentParser(grammar)

# Parse the sentence and generate parse trees
print("Parse Trees:")
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()  # Print the tree in a pretty format
