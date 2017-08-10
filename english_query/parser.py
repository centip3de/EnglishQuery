import sys
from lexer import Tokens
from builtin import *

class Parser():
    def __init__(self, tokens):
        self.tokens = tokens
        self.vars = {}


    def step(self):

        # TODO: Add error handling if `token == None`
        token = self.tokens[0]

        if token == Tokens.DEFINE:
            varName = self.tokens[2]
            classType = self.tokens[4]
            self.vars[varName] = classType()
            return classType

        elif token == Tokens.ASSIGNMENT:
            className = self.tokens[2]
            varName = self.tokens[4]
            value = self.tokens[5]
            setattr(self.vars[className], varName, value)
            return value

        elif token == Tokens.VAR_CREATION:
            className = self.tokens[2]
            varName = self.tokens[4]
            setattr(self.vars[className], varName, None)

        elif token == Tokens.WHAT_QUERY:
            className = self.tokens[2]
            varName = self.tokens[4]
            if varName in self.vars[className].__dict__.keys():
                return getattr(self.vars[className], varName)
            else:
                return None

        elif token == Tokens.WHERE_QUERY:
            className = self.tokens[2]
            return getattr(self.vars[className], 'location')

        elif token == Tokens.BI_RELATIONSHIP:
            firstVar = self.vars.get(self.tokens[2])
            secondVar = self.vars.get(self.tokens[4])
            if firstVar and secondVar:
                firstVar.relationship = secondVar
                secondVar.relationship = firstVar
                return str(firstVar) + " <=> " + str(secondVar)
            else:
                print("Could not establish a relationship", file=sys.stderr)

        elif token == Tokens.UNI_RELATIONSHIP:
            firstVar = self.vars.get(self.tokens[2])
            secondVar = self.vars.get(self.tokens[4])
            if firstVar and secondVar:
                firstVar.relationship = secondVar
                return str(firstVar) + " => " + str(secondVar)
            else:
                print("Could not establish a relationship", file=sys.stderr)

        else:
            print("[PARSER] Couldn't parse: " + token, file=sys.stderr)
            return None
