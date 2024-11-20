import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

# Download necessary NLTK resources
nltk.download('punkt')

def rule_based_pos_tagging(text):
    """
    Perform rule-based part-of-speech tagging using regular expressions.
    """
    # Define rules for tagging
    patterns = [
        (r'^[Tt]he$', 'DT'),       # Determiner
        (r'^[Aa]nd$', 'CC'),       # Coordinating conjunction
        (r'^[Ii]s$', 'VBZ'),       # Verb, 3rd person singular present
        (r'^[Ii]n$', 'IN'),        # Preposition
        (r'.*ing$', 'VBG'),        # Gerund/Present participle
        (r'.*ed$', 'VBD'),         # Past tense verb
        (r'.*es$', 'VBZ'),         # Verb, 3rd person singular present
        (r'.*s$', 'NNS'),          # Plural noun
        (r'.*ly$', 'RB'),          # Adverb
        (r'.*able$', 'JJ'),        # Adjective
        (r'.*ness$', 'NN'),        # Noun formed from adjective
        (r'.*ment$', 'NN'),        # Noun formed from verb
        (r'^[A-Z].*$', 'NNP'),     # Proper noun
        (r'.+', 'NN')              # Default to noun
    ]

    # Initialize the RegexpTagger with the defined patterns
    tagger = RegexpTagger(patterns)

    # Tokenize the text into words
    tokens = word_tokenize(text)

    # Perform POS tagging
    tagged_words = tagger.tag(tokens)

    # Print the results
    print(f"{'Word':<15}{'POS Tag'}")
    print("-" * 30)
    for word, tag in tagged_words:
        print(f"{word:<15}{tag}")


if __name__ == "__main__":
    # Example text
    input_text = """
    The quick brown fox jumps over the lazy dog. It is running swiftly and gracefully.
    """

    print("Rule-Based Part-of-Speech Tagging:")
    rule_based_pos_tagging(input_text)
