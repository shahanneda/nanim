class BasicObject:
    def __init__(self, points, color):
        self.points = points
        self.color = color

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class Rectangle(BasicObject):

    def __init__(self, x, y, width, height, color=Color(0,0,0)):
        super().__init__( [Point(x,y), Point(x+width, y), Point(x+width, y+height), Point(x,y+height)] , color);
        
