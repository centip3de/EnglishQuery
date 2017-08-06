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

class DefaultBuiltin():
    def __init__(self):
        pass
