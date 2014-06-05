"""
parse machine definition from json and supply method to retrieve machine
"""

import json


class parse():
    states = None
    alphabet = None
    transitions = None
    start = None
    accept = None
    
    #get path to file with machine encoding
    def __init__(self, encoding):
        pass

    #parse json to seperate pieces
    def parse(self):        
        pass

    #return machine definition
    def get_dfa(self):
        dfa = {}
        dfa['states'] = states
        dfa['alphabet'] = alphabet
        dfa['transitions'] = transitions
        dfa['start'] = start
        dfa['accept'] = accept
   
        return dfa

