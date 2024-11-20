class MorphologicalFSM:
    def __init__(self):
        # Define states and transitions
        self.transitions = {
            "start": self.handle_start,
            "add_s": self.add_s,
            "add_es": self.add_es,
            "replace_y": self.replace_y,
            "accept": self.accept
        }
        self.state = "start"  # Initial state
        self.result = ""  # Stores the transformed word

    def handle_start(self, word):
        """Determine the transition based on the last character(s)."""
        if word.endswith(("s", "x", "z", "ch", "sh")):
            self.state = "add_es"
        elif word.endswith("y") and not word[-2].lower() in "aeiou":
            self.state = "replace_y"
        else:
            self.state = "add_s"

    def add_s(self, word):
        """Add 's' to the word."""
        self.result = word + "s"
        self.state = "accept"

    def add_es(self, word):
        """Add 'es' to the word."""
        self.result = word + "es"
        self.state = "accept"

    def replace_y(self, word):
        """Replace the ending 'y' with 'ies'."""
        self.result = word[:-1] + "ies"
        self.state = "accept"

    def accept(self, word):
        """Accept state; do nothing."""
        pass

    def generate_plural(self, word):
        """Generate the plural form of the given word."""
        self.state = "start"
        self.result = ""
        while self.state != "accept":
            self.transitions[self.state](word)
        return self.result


# Example usage
if __name__ == "__main__":
    fsm = MorphologicalFSM()

    # Test words
    words = [
        "cat",    # Regular plural
        "dog",    # Regular plural
        "bus",    # Ends with 's'
        "box",    # Ends with 'x'
        "buzz",   # Ends with 'z'
        "church", # Ends with 'ch'
        "brush",  # Ends with 'sh'
        "baby",   # Ends with consonant + 'y'
        "toy",    # Ends with vowel + 'y'
    ]

    print("Morphological Parsing (Pluralization):")
    for word in words:
        plural = fsm.generate_plural(word)
        print(f"{word} -> {plural}")
