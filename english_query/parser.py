from lexer import Tokens
from builtin import *

class Parser():
    def __init__(self, tokens):
        self.tokens = tokens
        self.vars = {}


    def step(self):
        token = self.tokens[0]

        if token == Tokens.DEFINE:
            varName = self.tokens[2]
            classType = self.tokens[4]
            self.vars[varName] = classType()
            return classType

        elif token == Tokens.CLASS:
            className = self.tokens[1]
            varName = self.tokens[3]
            value = None
            if len(self.tokens) == 6:
                value = self.tokens[5]

            setattr(self.vars[className], varName, value)
            return value

        elif token == Tokens.WHAT_QUERY:
            className = self.tokens[2]
            varName = self.tokens[4]
            return getattr(self.vars[className], varName)

        elif token == Tokens.WHERE_QUERY:
            className = self.tokens[2]
            return getattr(self.vars[className], 'location')
