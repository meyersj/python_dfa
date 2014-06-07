import json

DESC = "description"
STATE = "states"
START = "start"
ALPHA = "alphabet"
TRANS = "transitions"
ACCEPT = "accept"
INPUTS = "inputs"


class DFA:
    states = []
    alphabet = []
    description = ""
    start_state = ""
    accept_states = []
    # {State : {input : newState}}
    transitions = {"": {"" : ""}}
    input_strings = []
    
    def __init__(self, file_name):
        dfa = json.load(open(file_name))
        self.states = dfa[STATE]
        self.alphabet = dfa[ALPHA]
        self.description = dfa[DESC]
        self.start_state = dfa[START]
        self.accept_states = dfa[ACCEPT]
        self.transitions = dfa[TRANS]
        self.input_strings = dfa[INPUTS]

    def get_dfa(self):
    	return self, self.input_strings

    def run_dfa(self, input_str):
        current_state = self.start_state
        print "Running the DFA with the description:"
        print self.description
        print "On the input: " + input_str

        for char in input_str:
            if current_state not in self.transitions:
                print "Invalid DFA: " + current_state + " is not a state in the DFA."
                return

            if char not in self.transitions[current_state]:
                print "Invalid DFA: " + char + " does not transition to a state in the DFA."
                return

            new_state = self.transitions[current_state][char]
            print "Moving from state: " + current_state + " to State: " + new_state + " on input: " + char
            current_state = new_state

        if any(current_state in s for s in self.accept_states):
            print "The DFA ACCEPTS the input: " + input_str + "\n"
        else:
            print "The DFA REJECTS the input: " + input_str + "\n"


if __name__ == "__main__":
    dfa, input_strings = DFA("machine1.json").get_dfa()

    for s in input_strings:
    	dfa.run_dfa(s)

    dfa, input_strings = DFA("machine2.json").get_dfa()

    for s in input_strings:
        dfa.run_dfa(s)

