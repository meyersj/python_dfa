"""
Authors:
  
  Jeffrey Meyers
  Ruben Niculcea

Date:
  
  June 7, 2014

Purpose:
  
  Extra credit assignment for CS 311 - Computational Structures
  taught by Daniel Leblanc at Portland State University.

  Implement a program takes as input an encoding of a DFA machine and a string
  and states whether the string is a member of the language defined
  by that machine.

Description:
  
  1. The DFA class is intialized with a path to an encoding of a DFA as JSON.

  2. The JSON is parsed into the 5 parts required to define a DFA in addition
  to a description of the machine and an array containing test inputs.

  3. The machine and test inputs are returned after parsing.

  4. The machine runs on each input and prints the transitions taken
  and after all characters are consumed prints whether it is in an ACCEPT
  state.

"""

import json

DESC = "description"
STATE = "states"
START = "start"
ALPHA = "alphabet"
TRANS = "transitions"
ACCEPT = "accept"
INPUTS = "inputs"


class DFA:
    states = None
    alphabet = None
    description = None
    start_state = None
    accept_states = None
    # {State : {input : newState}}
    transitions = None
    input_strings = None 
    
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
    
    # machine 1 accepts substrings 'aba'
    dfa, input_strings = DFA("machine1.json").get_dfa()

    for s in input_strings:
    	dfa.run_dfa(s)

    # machine 2 accepts binary multiples of 3
    dfa, input_strings = DFA("machine2.json").get_dfa()

    for s in input_strings:
        dfa.run_dfa(s)

    # machine 3 accepts the substrings 'jeff' or 'ruben'
    dfa, input_strings = DFA("machine3.json").get_dfa()

    for s in input_strings:
        dfa.run_dfa(s)

