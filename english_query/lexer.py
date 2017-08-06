from enum import Enum
from builtin import *

class Tokens(Enum):
    DEFINE = 0,
    ASSIGNMENT = 1,
    TYPE = 2,
    NAME = 3,
    FIELD = 4,
    WHAT_QUERY = 5,
    CLASS = 6,
    VAR = 7,
    VAR_CREATION = 8,
    CLASS_CREATION = 9,
    WHERE_QUERY = 10,
    HOW_QUERY = 11


class Lexer():
    def __init__(self, text):
        self.text = text
        self.vars = {}
        self.query_strings = ["where", "what", "who", "when", "how"]

    def createClass(self, name):
        return type(name, (DefaultBuiltin,), {})

    def getClass(self, name, objType):
        if objType == Types.OBJECT:
            return ObjectBuiltin
        elif objType == Types.FOOD:
            return FoodBuiltin
        else:
            return self.createClass(name)

    def getType(self, token):
        if token == "object":
            return Types.OBJECT
        elif token == "food":
            return Types.FOOD
        else:
            return None

    def step(self, tokens):
        token = tokens[0]

        if token == "define":
            name = tokens[1]
            objName = tokens[4]
            objType = self.getType(objName)

            objType = self.getClass(objName, objType)
            self.vars[name] = objType
            return (Tokens.DEFINE, Tokens.NAME, name, Tokens.TYPE, objType)

        elif self.vars.get(token):
            assignment = tokens[1] + " " + tokens[2]
            if assignment == "has a" or assignment == "has an":
                varName = tokens[3]

                if len(tokens) == 6:
                    return (Tokens.CLASS, token,
                            Tokens.VAR, varName,
                            Tokens.ASSIGNMENT, tokens[5])
                else:
                    return (Tokens.CLASS, token,
                            Tokens.VAR, varName,
                            Tokens.VAR_CREATION)

        elif token in self.query_strings:
            className = tokens[2].rstrip("'s")
            className = tokens[2].rstrip("'s?")

            if self.vars.get(className):
                if token == "where":
                    return (Tokens.WHERE_QUERY,
                            Tokens.CLASS, className)
                else:
                    varName = tokens[3].rstrip('?')
                    return (Tokens.WHAT_QUERY,
                            Tokens.CLASS, className,
                            Tokens.VAR, varName)
            else:
                print("[LEXER] Unknown class: " + className, file=sys.stderr)

        else:
            print("[LEXER] Couldn't lex: " + token, file=sys.stderr)
            return (None)

    def lex(self):
        return self.step(self.text.split(" "))
