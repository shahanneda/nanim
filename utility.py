class BasicObject:
    def __init__(self, points, color):
        self.points = points
        self.color = color


    def insert_animation_into_frame(self, function, parameters, i):
        while len(self.scene.frames) <= i:
            self.scene.frames.append([])
        self.scene.frames[i].append([function, parameters]); 

    
class Shape(BasicObject):
    def move_to(self, point, time, starting_time=0):
        startingFrame = starting_time * self.scene.FRAME_RATE
        totalFrames = startingFrame + time * self.scene.FRAME_RATE;
    
        for i in range(int(startingFrame), int(totalFrames)):
            prog = (i-startingFrame)/(int(totalFrames)-int(startingFrame));
            self.insert_animation_into_frame(self.change_coord, [Point(point.x * prog, point.y * prog)], i ); 
    
    def change_coord(self, point):
        self.setX(point.x);
        self.setY(point.y);

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class Rectangle(Shape):

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

        
