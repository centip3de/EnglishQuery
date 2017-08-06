from enum import Enum

class Color(Enum):
    NONE = "none",
    RED = "red",
    BLUE = "blue",
    GREEN = "green",
    YELLOW = "yellow",
    ORANGE = "orange",
    PURPLE = "purple",
    PINK = "pink",
    WHITE = "white",
    BLACK = "black"

class Types(Enum):
    OBJECT = 0,
    FOOD = 1,

class Tokens(Enum):
    DEFINE = 0,
    ASSIGNMENT = 1,
    TYPE = 2,
    NAME = 3,
    FIELD = 4,
    QUERY = 5,
    CLASS = 6,
    VAR = 7,
    VAR_CREATION = 8,
    CLASS_CREATION = 9

class FoodBuiltin():
    def __init__(self):
        pass

class ObjectBuiltin():
    def __init__(self,
                 name="",
                 location=(0, 0),
                 color=Color.NONE,
                 size=0,
                 parent=None):

        self.name = name
        self.location = location
        self.color = color
        self.size = size
        self.parent = parent
        self.location_type = type(location)

class Lexer():
    def __init__(self, text):
        self.text = text
        self.vars = {}
        self.query_strings = ["where", "what", "who", "when", "how"]

    def createClass(self, name):
        return None

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

        if token == "Define":
            name = tokens[1].lower()
            objName = tokens[4].lower()
            objType = self.getType(objName)

            objType = self.getClass(objName, objType)
            self.vars[name] = objType
            return (Tokens.DEFINE, Tokens.NAME, name, Tokens.TYPE, objType)

        elif self.vars.get(token.lower()):
            assignment = tokens[1] + " " + tokens[2]
            if assignment == "has a":
                varName = tokens[3]

                if len(tokens) == 6:
                    return (Tokens.CLASS, token.lower(),
                            Tokens.VAR, varName,
                            Tokens.ASSIGNMENT, tokens[5])
                else:
                    return (Tokens.CLASS, token.lower(),
                            Tokens.VAR, varName,
                            Tokens.VAR_CREATION)

    def lex(self):
        return self.step(self.text.split(" "))
