import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

# Define the Probabilistic Context-Free Grammar (PCFG)
pcfg_grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.6] | Det Adj N [0.4]
    VP -> V NP [0.7] | V [0.3]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'dog' [0.5] | 'cat' [0.5]
    Adj -> 'big' [0.8] | 'small' [0.2]
    V -> 'saw' [0.6] | 'likes' [0.4]
""")

# Define the input sentence
sentence = "the big dog saw a cat".split()

# Create a parser using the Viterbi algorithm
parser = ViterbiParser(pcfg_grammar)

# Parse the sentence and print the most probable parse tree
print("Most Probable Parse Tree:")
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
