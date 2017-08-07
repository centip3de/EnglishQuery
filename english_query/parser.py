import sys
from lexer import Tokens
from builtin import *

class Parser():
    def __init__(self, tokens):
        self.tokens = tokens
        self.vars = {}


    # TODO: We need to refactor what our lexer spits out. Right now
    # it's unclear what is happening from the first token, when we should
    # be able to easily differentiate.
    def step(self):

        # TODO: Add error handling if `token == None`
        token = self.tokens[0]

        # Definition
        if token == Tokens.DEFINE:
            varName = self.tokens[2]
            classType = self.tokens[4]
            self.vars[varName] = classType()
            return classType

        # Assignment
        elif token == Tokens.CLASS:
            className = self.tokens[1]
            varName = self.tokens[3]
            value = None
            if len(self.tokens) == 6:
                value = self.tokens[5]

            setattr(self.vars[className], varName, value)
            return value

        # Lookup
        elif token == Tokens.WHAT_QUERY:
            className = self.tokens[2]
            varName = self.tokens[4]
            if varName in self.vars[className].__dict__.keys():
                return getattr(self.vars[className], varName)
            else:
                return None

        # Alternative lookup
        elif token == Tokens.WHERE_QUERY:
            className = self.tokens[2]
            return getattr(self.vars[className], 'location')

        # Relationship
        elif token == Tokens.VAR:
            firstVar = self.vars.get(self.tokens[1])
            secondVar = self.vars.get(self.tokens[4])
            relationship_type = self.tokens[2]

            if firstVar and secondVar:
                if relationship_type == Tokens.UNI_RELATIONSHIP:
                    firstVar.relationship = secondVar
                    return str(firstVar) + " => " + str(secondVar)

                elif relationship_type == Tokens.BI_RELATIONSHIP:
                    firstVar.relationship = secondVar
                    secondVar.relationship = firstVar
                    return str(firstVar) + " <=> " + str(secondVar)
            else:
                print("[PARSER] Couldn't establish relationship between " + str(firstVar) + " and " + str(secondVar), file=sys.stderr)

        else:
            print("[PARSER] Couldn't parse: " + token, file=sys.stderr)
            return None
