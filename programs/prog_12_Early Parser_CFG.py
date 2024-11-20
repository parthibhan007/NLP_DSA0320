from collections import defaultdict, namedtuple

# Representing a state in the Earley Chart
State = namedtuple("State", ["lhs", "rhs", "dot", "start", "end"])

class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.chart = []

    def parse(self, input_string, start_symbol):
        self.input = input_string.split()
        self.n = len(self.input)
        self.chart = [set() for _ in range(self.n + 1)]

        # Add initial state
        self.chart[0].add(State(start_symbol, tuple(["."] + self.grammar[start_symbol][0]), 0, 0, 0))

        # Process chart columns
        for i in range(self.n + 1):
            changes = True
            while changes:  # Keep iterating until no more states can be added
                changes = False
                current_states = list(self.chart[i])
                for state in current_states:
                    if self._is_complete(state):
                        changes |= self._completer(state, i)
                    elif self._is_non_terminal(state):
                        changes |= self._predictor(state, i)
                    else:
                        changes |= self._scanner(state, i)

        # Check if the final state is valid
        for state in self.chart[self.n]:
            if state.lhs == start_symbol and state.dot == len(state.rhs):
                return True
        return False

    def _is_complete(self, state):
        return state.dot == len(state.rhs)

    def _is_non_terminal(self, state):
        return state.rhs[state.dot] in self.grammar

    def _predictor(self, state, index):
        changes = False
        non_terminal = state.rhs[state.dot]
        for production in self.grammar[non_terminal]:
            new_state = State(non_terminal, tuple(["."] + production), 0, index, index)
            if new_state not in self.chart[index]:
                self.chart[index].add(new_state)
                changes = True
        return changes

    def _scanner(self, state, index):
        changes = False
        if index < self.n and self.input[index] == state.rhs[state.dot]:
            new_state = State(state.lhs, state.rhs, state.dot + 1, state.start, index + 1)
            if new_state not in self.chart[index + 1]:
                self.chart[index + 1].add(new_state)
                changes = True
        return changes

    def _completer(self, state, index):
        changes = False
        for prev_state in self.chart[state.start]:
            if prev_state.dot < len(prev_state.rhs) and prev_state.rhs[prev_state.dot] == state.lhs:
                new_state = State(prev_state.lhs, prev_state.rhs, prev_state.dot + 1, prev_state.start, index)
                if new_state not in self.chart[index]:
                    self.chart[index].add(new_state)
                    changes = True
        return changes


# Example Grammar
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"], ["V"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"]],
    "V": [["saw"], ["liked"]]
}

# Input string and start symbol
input_string = "the cat saw a dog"
start_symbol = "S"

# Parse
parser = EarleyParser(grammar)
if parser.parse(input_string, start_symbol):
    print("The input string is valid!")
else:
    print("The input string is invalid.")
