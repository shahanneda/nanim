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
        self.x = x;
        self.y = y;
        self.width = width;
        self.height = height;

        super().__init__( self.calcPoints(), color);

    def calcPoints(self):
        return [Point(self.x,self.y), Point(self.x+self.width, self.y), Point(self.x+self.width, self.y+self.height), Point(self.x,self.y+self.height)]

    def setY(self, y):
        self.y = y;
        self.points = self.calcPoints();

    def setX(self, x):
        self.x = x;
        self.points = self.calcPoints();

        
