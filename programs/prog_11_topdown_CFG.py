class TopDownParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.tokens = []
        self.current_token_index = 0

    def parse(self, start_symbol, input_string):
        self.tokens = input_string.split()
        self.current_token_index = 0
        if self._parse_symbol(start_symbol):
            if self.current_token_index == len(self.tokens):  # Check if all tokens are consumed
                return True
            else:
                print("Error: Unconsumed tokens remaining.")
        return False

    def _parse_symbol(self, symbol):
        if symbol in self.grammar:  # Non-terminal
            for production in self.grammar[symbol]:
                saved_index = self.current_token_index
                if all(self._parse_symbol(sym) for sym in production):
                    return True
                self.current_token_index = saved_index  # Backtrack
            return False
        else:  # Terminal
            if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index] == symbol:
                self.current_token_index += 1
                return True
            return False


# Example Grammar
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"], ["V"]],
    "Det": [["a"], ["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["saw"], ["liked"]]
}

# Input example
input_string = "the cat saw a dog"
parser = TopDownParser(grammar)

if parser.parse("S", input_string):
    print("Input string is valid according to the grammar!")
else:
    print("Input string is invalid.")
