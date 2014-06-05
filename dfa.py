class dfa:
    start_state = ""
    accept_states = []
    # {State : {input : newState}}
    transitions = {"": {"" : ""}}

    def dfa(self, start_state, accept_states, transitions):
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions

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

