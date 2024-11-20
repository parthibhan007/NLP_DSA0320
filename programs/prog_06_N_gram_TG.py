import random
from collections import defaultdict

class BigramModel:
    def __init__(self):
        self.bigram_counts = defaultdict(lambda: defaultdict(int))
        self.start_words = []

    def train(self, text):
        """
        Train the bigram model using input text.
        """
        words = text.split()
        self.start_words.append(words[0])  # Collect potential starting words
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            self.bigram_counts[current_word][next_word] += 1

    def generate_text(self, length=10):
        """
        Generate text using the trained bigram model.
        """
        # Start with a random word
        current_word = random.choice(self.start_words)
        generated_words = [current_word]

        for _ in range(length - 1):
            next_words = list(self.bigram_counts[current_word].items())
            if not next_words:
                break  # Stop if there are no next words
            next_word = random.choices(
                [word for word, count in next_words],
                [count for word, count in next_words]
            )[0]
            generated_words.append(next_word)
            current_word = next_word

        return ' '.join(generated_words)


if __name__ == "__main__":
    # Example training text
    input_text = """
    The quick brown fox jumps over the lazy dog. The lazy dog barks at the quick fox. 
    The fox is clever and the dog is loyal.
    """

    # Initialize and train the bigram model
    model = BigramModel()
    model.train(input_text)

    # Generate text using the trained bigram model
    print("Generated Text:")
    print(model.generate_text(length=15))
