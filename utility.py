class BasicObject:
    def __init__(self, points):
        self.points = points

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(BasicObject):
    def __init__(self, x, y, width, height):
        super().__init__(points=[Point(x,y), Point(x+width, y), Point(x+width, y+height), Point(x,y+height)]);
        
class Color:
    def __init__(r, g, b):
        self.r = r
        self.g = g
        self.b = b
