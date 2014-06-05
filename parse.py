"""
parse machine definition from json and supply method to retrieve machine
"""
import json

DESC = "description"
STATE = "states"
START = "start"
ALPHA = "alphabet"
TRANS = "transitions"
ACCEPT = "accept"

class parse():
    dfa = {}
    
    def __init__(self, json_file):
        json_data = open(json_file)
        data = json.load(json_data)
        self.__parse(data)

    def __parse(self, data):        
        self.dfa[DESC] = data[DESC]
        self.dfa[STATE] = data[STATE]
        self.dfa[ALPHA] = data[ALPHA]
        self.dfa[TRANS] = data[TRANS] 
        self.dfa[START] = data[START]
        self.dfa[ACCEPT] = data[ACCEPT]
        
    def get_dfa(self):
        return self.dfa
    

if __name__ == "__main__":
    json_file = "machine1.json"
    parse = parse(json_file)
    dfa = parse.get_dfa()
    
    print
    print "Description: " + dfa[DESC]
    print
    print "Start at '{0}'".format(dfa[START])
    print
    for state in dfa[STATE]:
        print "State: " + state
         
        for letter in dfa[ALPHA]:
            output = "  On '{0}' transition to '{1}'" 
            print output.format(letter, dfa[TRANS][state][letter])
    print
    print "Accept if string terminates in.."
    for state in dfa[ACCEPT]:
        print state 
