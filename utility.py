class BasicObject:
    animationIdCount = 0
    def __init__(self, points, color):
        self.points = points
        self.color = color
        self.old_animation_positions = {}
        self.lastAnimationTime = 0;

    def insert_animation_into_frame(self, function, parameters, i):
        while len(self.scene.frames) <= i:
            self.scene.frames.append([])
        self.scene.frames[i].append([function, parameters]); 

    def get_anim_frames(self, time, starting_time):
        startingFrame = starting_time * self.scene.FRAME_RATE
        totalFrames = startingFrame + time * self.scene.FRAME_RATE;
        return (int(round(startingFrame)), int(round(totalFrames)))
    
    def get_prog(self,index, startingFrame, lastFrame):
        if(index >= startingFrame):
            pass
            #return 1
        return float((index-int(startingFrame))/(int(lastFrame)-int(startingFrame)))

    def fadeOut(self, duration=0.5, starting_time="not_set", blocking=True):
        if starting_time == "not_set":
            starting_time = self.lastAnimationTime;
        startingFrame, lastFrame = self.get_anim_frames(duration, starting_time);
        for i in range(startingFrame, lastFrame+1):
            alpha = 1-self.get_prog(i, startingFrame, lastFrame)
            self.insert_animation_into_frame(self.set_color, [Color(self.color.r, self.color.g, self.color.b,alpha)], i ); 

        if blocking:
            self.lastAnimationTime = starting_time + duration;
        return self
    def fadeIn(self, duration=0.5, starting_time="not_set", blocking=True):
        if starting_time == "not_set":
            starting_time = self.lastAnimationTime;
        startingFrame, lastFrame = self.get_anim_frames(duration, starting_time);
        for i in range(startingFrame, lastFrame+1):
            alpha = self.get_prog(i, startingFrame, lastFrame)
            self.insert_animation_into_frame(self.set_color, [Color(self.color.r, self.color.g, self.color.b,alpha)], i ); 

        if blocking:
            self.lastAnimationTime = starting_time + duration;

        return self

    def set_color(self,color):
        self.color = color;
def lin_interpolate(x1, y1, x2, y2, x3):
    return y1 + (x3 - x1) * ((y2-y1)/(x2-x1))

class Shape(BasicObject):

    def move_to(self, point, duration, starting_time="not_set"):
        if starting_time == "not_set":
            starting_time = self.lastAnimationTime
        startingFrame, lastFrame = self.get_anim_frames(duration, starting_time);
        for i in range(startingFrame, lastFrame+1):
            self.insert_animation_into_frame(self.lerp_to, [point, startingFrame, lastFrame,i, BasicObject.animationIdCount], i ); 
        
        BasicObject.animationIdCount += 1;
        self.lastAnimationTime = starting_time+duration;
        return self
    
    def lerp_to(self, final_point, first_frame, last_frame, current_frame_index, animation_id):
            starting_x = 0;
            starting_y = 0;
        
            print(f" last {last_frame} current : {current_frame_index}") 
            if animation_id in self.old_animation_positions:
                starting_x, starting_y = self.old_animation_positions[animation_id];
            else:
                starting_x = self.x;
                starting_y = self.y;
                self.old_animation_positions[animation_id] = (self.x, self.y);

            lerped_x = lin_interpolate(first_frame, starting_x, last_frame, final_point.x, current_frame_index) ## we dont want current position, we want intial posisiton 
            lerped_y = lin_interpolate(first_frame, starting_y, last_frame, final_point.y, current_frame_index)
            self.change_coord(Point(lerped_x, lerped_y));

            #print(f"final point = {final_point.x} {final_point.y} current pos = {self.x} {self.y}" )
            #print(f"moving to {lerped_x} y {lerped_y}");

    def change_coord(self, point):
        self.setX(point.x);
        self.setY(point.y);

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Color:
    def __init__(self, r, g, b, a=1):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

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

        
