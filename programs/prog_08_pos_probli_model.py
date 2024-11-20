import nltk
from collections import defaultdict, Counter
import random

# Download necessary data
nltk.download('brown')
nltk.download('universal_tagset')

class SimplePOSTagger:
    def __init__(self):
        self.transition_probs = defaultdict(Counter)  # Transition probabilities (tag -> next_tag)
        self.emission_probs = defaultdict(Counter)  # Emission probabilities (tag -> word)
        self.tag_counts = Counter()  # Counts of each tag

    def train(self, tagged_sentences):
        """
        Train the tagger using tagged sentences.
        """
        for sentence in tagged_sentences:
            previous_tag = "<START>"
            for word, tag in sentence:
                # Update transition probabilities
                self.transition_probs[previous_tag][tag] += 1

                # Update emission probabilities
                self.emission_probs[tag][word.lower()] += 1

                # Update tag counts
                self.tag_counts[tag] += 1

                # Update previous tag
                previous_tag = tag

            # Handle end of sentence transition
            self.transition_probs[previous_tag]["<END>"] += 1

    def predict(self, sentence):
        """
        Predict POS tags for a given sentence using a stochastic approach.
        """
        previous_tag = "<START>"
        tags = []

        for word in sentence:
            word_lower = word.lower()
            
            # Calculate emission probabilities for the current word
            tag_probs = {
                tag: (self.transition_probs[previous_tag][tag] / sum(self.transition_probs[previous_tag].values())) *
                     (self.emission_probs[tag][word_lower] / sum(self.emission_probs[tag].values()))
                for tag in self.emission_probs
            }

            # Select the tag with the highest probability
            if tag_probs:
                predicted_tag = max(tag_probs, key=tag_probs.get)
            else:
                # Default to the most common tag if no probabilities are available
                predicted_tag = max(self.tag_counts, key=self.tag_counts.get)

            tags.append(predicted_tag)
            previous_tag = predicted_tag

        return tags


if __name__ == "__main__":
    # Load tagged sentences from the Brown corpus
    tagged_sentences = nltk.corpus.brown.tagged_sents(tagset="universal")

    # Split data into training and testing sets
    train_data = tagged_sentences[:40000]
    test_data = tagged_sentences[40000:40200]

    # Initialize and train the tagger
    tagger = SimplePOSTagger()
    tagger.train(train_data)

    # Test the tagger on a sentence
    test_sentence = [word for word, tag in test_data[0]]  # Extract a test sentence
    print("Input Sentence:", " ".join(test_sentence))

    predicted_tags = tagger.predict(test_sentence)
    print("\nPredicted POS Tags:")
    print(predicted_tags)

    # Compare with actual tags
    actual_tags = [tag for word, tag in test_data[0]]
    print("\nActual POS Tags:")
    print(actual_tags)
