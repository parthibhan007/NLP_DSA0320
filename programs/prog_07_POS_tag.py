import nltk

# Download required NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):
    """
    Perform Part-of-Speech tagging on the input text.
    """
    # Tokenize the text into words
    tokens = nltk.word_tokenize(text)
    
    # Perform POS tagging
    tagged_words = nltk.pos_tag(tokens)
    
    # Print the results
    print(f"{'Word':<15}{'POS Tag'}")
    print("-" * 30)
    for word, tag in tagged_words:
        print(f"{word:<15}{tag}")


if __name__ == "__main__":
    # Example input text
    input_text = """
    The quick brown fox jumps over the lazy dog. 
    She sells seashells by the seashore. 
    The rain in Spain stays mainly in the plain.
    """
    
    print("Part-of-Speech Tagging:")
    pos_tagging(input_text)
