DESC = "description"
STATE = "states"
START = "start"
ALPHA = "alphabet"
TRANS = "transitions"
ACCEPT = "accept"
INPUTS = "inputs"

class dfa:
    states = []
    description = ""
    start_state = ""
    accept_states = []
    # {State : {input : newState}}
    transitions = {"": {"" : ""}}
    
    def dfa(self, file_name):
        parse = parse(file_name)
        dfa = parse.get_dfa()
        self.states = dfa[STATES]
        self.start_state = dfa[START]
        self.accept_states = dfa[ACCEPT]
        self.transitions = dfa[TRANS]
        
        for input_str in dfa[INPUTS]
            run_dfa(input_str)

    def run_dfa(input_str):
        current_state = self.start_state
        print "Running the DFA on the input: " + str(input_str)

        for char in input_str:
            if current_state not in transitions:
                print str(current_state) + " is not a state in the DFA."
                return

            if char not in transitions[current_state]:
                print str(char) + " does not transition to a state in the DFA."
                return

            new_state = transitions[current_state][char]
            print "Moving from state: " + str(current_state) + " to State: " + str(new_state) + " on input: " + str(char)
            current_state = new_state

        if any(current_state in s for s in accept_states):
            print "The DFA aceepts the input: " + str(input_str)
        else:
            print "The DFA does not aceept the input: " + str(input_str)

