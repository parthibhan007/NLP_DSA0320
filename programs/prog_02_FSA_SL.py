class FiniteStateAutomaton:
    def __init__(self):
        # Define states and transitions
        self.states = {
            0: {'a': 1},
            1: {'b': 2},
            2: {}  # Accept state, no outgoing transitions needed
        }
        self.start_state = 0
        self.accept_state = 2
        self.current_state = self.start_state

    def reset(self):
        """Reset the automaton to the start state."""
        self.current_state = self.start_state

    def process(self, string):
        """
        Process the input string character by character.
        Return True if the string ends in 'ab', otherwise False.
        """
        self.reset()
        for char in string:
            if char in self.states[self.current_state]:
                self.current_state = self.states[self.current_state][char]
            else:
                self.current_state = self.start_state  # Reset on invalid input

        return self.current_state == self.accept_state


# Example usage
if __name__ == "__main__":
    fsa = FiniteStateAutomaton()

    test_strings = [
        "helloab",   # Ends with 'ab' - should match
        "abab",      # Ends with 'ab' - should match
        "hello",     # Does not end with 'ab' - no match
        "a",         # Does not end with 'ab' - no match
        "b",         # Does not end with 'ab' - no match
        "abcab",     # Ends with 'ab' - should match
    ]

    for string in test_strings:
        result = fsa.process(string)
        print(f"'{string}' -> {'Matched' if result else 'Not Matched'}")
