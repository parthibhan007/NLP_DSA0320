import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

def morphological_analysis(text):
    # Tokenize the input text
    words = word_tokenize(text)

    # Initialize stemmer and lemmatizer
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    # Perform stemming and lemmatization
    print(f"{'Word':<15}{'Stemmed':<15}{'Lemmatized'}")
    print("-" * 40)
    for word in words:
        stemmed = stemmer.stem(word)
        lemmatized = lemmatizer.lemmatize(word)
        print(f"{word:<15}{stemmed:<15}{lemmatized}")

if __name__ == "__main__":
    # Input text for analysis
    input_text = """
    Running runners ran quickly. 
    The foxes are jumping over the fences.
    She studies hard to improve her studying.
    """
    
    print("Morphological Analysis:")
    morphological_analysis(input_text)
