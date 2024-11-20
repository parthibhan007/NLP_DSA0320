from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download NLTK data if needed (uncomment the next line if required)
# import nltk
# nltk.download('punkt')

def stem_words(words):
    # Initialize the Porter Stemmer
    porter_stemmer = PorterStemmer()
    
    print(f"{'Word':<15}{'Stemmed'}")
    print("-" * 25)
    
    # Perform stemming for each word
    for word in words:
        stemmed = porter_stemmer.stem(word)
        print(f"{word:<15}{stemmed}")


if __name__ == "__main__":
    # List of words to stem
    word_list = [
        "running", "jumps", "easily", "studying", 
        "flies", "runningly", "connected", "connectivity", 
        "happiness", "relational", "demonstration"
    ]
    
    print("Word Stemming using Porter Stemmer:")
    stem_words(word_list)
