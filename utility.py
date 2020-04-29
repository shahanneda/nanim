class BasicObject:
    def __init__(self, points, color):
        self.points = points
        self.color = color


    def insert_animation_into_frame(self, function, parameters, i):
        while len(self.scene.frames) <= i:
            self.scene.frames.append([])
        self.scene.frames[i].append([function, parameters]); 

    def get_anim_frames(self, time, starting_time):
        startingFrame = starting_time * self.scene.FRAME_RATE
        totalFrames = startingFrame + time * self.scene.FRAME_RATE;
        return (startingFrame, totalFrames)
    
    def get_prog(self,index, startingFrame, lastFrame):
        if(index >= startingFrame):
            pass
            #return 1
        return float((index-int(startingFrame))/(int(lastFrame)-int(startingFrame)))

def lin_interpolate(x1, y1, x2, y2, x3):
    return y1 + (x3 - x1) * ((y2-y1)/(x2-x1))

class Shape(BasicObject):
    def move_to(self, point, duration, starting_time=0):
        startingFrame , lastFrame = self.get_anim_frames(duration, starting_time); 
        for i in range(int(startingFrame), int(lastFrame)):
            prog = self.get_prog(i, startingFrame, lastFrame)

            self.insert_animation_into_frame(self.lerp_to, [point, startingFrame, lastFrame,i], i ); 
    
    def lerp_to(self, final_point, first_frame, last_frame, current_frame_index):
            lerped_x = lin_interpolate(first_frame, self.x, last_frame, final_point.x, current_frame_index) 
            lerped_y = lin_interpolate(first_frame, self.y, last_frame, final_point.y, current_frame_index)
            self.change_coord(Point(lerped_x, lerped_y));

            print(f"final point = {final_point.x} {final_point.y} current pos = {self.x} {self.y}" )
            print(f"moving to {lerped_x} y {lerped_y}");

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

        
