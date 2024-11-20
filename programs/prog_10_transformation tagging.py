import nltk
from nltk.tag import UnigramTagger, RegexpTagger
from nltk.corpus import treebank
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download('treebank')
nltk.download('punkt')

class TransformationBasedTagger:
    def __init__(self, initial_tagger):
        """
        Initialize with a baseline tagger.
        """
        self.initial_tagger = initial_tagger
        self.transformation_rules = []

    def apply_rule(self, rule, tagged_sentence):
        """
        Apply a single transformation rule to a tagged sentence.
        """
        for i, (word, tag) in enumerate(tagged_sentence):
            if rule['condition'](word, tag, i, tagged_sentence):
                tagged_sentence[i] = (word, rule['new_tag'])
        return tagged_sentence

    def tag(self, sentence):
        """
        Tag a sentence using the baseline tagger and transformation rules.
        """
        tagged_sentence = self.initial_tagger.tag(sentence)
        for rule in self.transformation_rules:
            tagged_sentence = self.apply_rule(rule, tagged_sentence)
        return tagged_sentence

    def add_rule(self, condition, new_tag):
        """
        Add a new transformation rule.
        """
        self.transformation_rules.append({'condition': condition, 'new_tag': new_tag})


if __name__ == "__main__":
    # Training a unigram tagger as the baseline tagger
    training_sentences = treebank.tagged_sents()
    baseline_tagger = UnigramTagger(training_sentences)

    # Initialize the transformation-based tagger
    tbt = TransformationBasedTagger(initial_tagger=baseline_tagger)

    # Add a simple transformation rule
    # Example rule: If a word is "is" and tagged as NN, change the tag to VBZ
    tbt.add_rule(
        condition=lambda word, tag, index, sentence: word.lower() == 'is' and tag == 'NN',
        new_tag='VBZ'
    )

    # Input sentence for tagging
    sentence = word_tokenize("This is a test sentence.")

    # Apply the transformation-based tagger
    tagged_sentence = tbt.tag(sentence)

    # Display the results
    print("Tagged Sentence:")
    for word, tag in tagged_sentence:
        print(f"{word:<10}{tag}")
