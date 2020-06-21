import math;
class BasicObject:
    animationIdCount = 0
    def __init__(self, points, color):
        self.points = points
        self.color = color
        self.old_animation_positions = {} # this is used during the animation rendering procces inorder to keep track of the last position and lerp from there for example in lerp
        self.lastAnimationTime = 0;
        self.recalculate_position_from_points()# if after a wierd roation there is a shape we can average out the x and y from the points
        self.running_positions = {"color": color} ## this is strore certain things inorder to allow the user to do thing like translate before the rendering procces

    """ This helper function adds a function to be run with parameters given in an array in a certain index."""
    def insert_animation_into_frame(self, function, parameters, i):
        while len(self.scene.frames) <= i:
            self.scene.frames.append([])
        self.scene.frames[i].append([function, parameters]); 

    """ Returns an objects current position, can be used for rotating around other object. """ 
    def get_position(self):
        return Point(self.running_positions["x"], self.running_positions["y"]);

    """ 
    Give a starting time and duration retuns the frame number of the first and last frame in a tuple (first_frame_number, last_fram\e_number) 
    """
    def get_anim_frames(self, time, starting_time):
        startingFrame = starting_time * self.scene.FRAME_RATE
        totalFrames = startingFrame + time * self.scene.FRAME_RATE;
        return (int(round(startingFrame)), int(round(totalFrames)))
    """ Can be used to check how far along certain animation we are, used for fade in and outs """ 
    def get_prog(self,index, startingFrame, lastFrame):
        if(index >= startingFrame):
            pass
        #return 1
        return float((index-int(startingFrame))/(int(lastFrame)-int(startingFrame)))
    """ Called by the animation frame runner """
    def anim_set_color(self, color): 
        starting_color = color;
        self.color = color

    def fade_out(self, duration=0.5, starting_time="not_set", blocking=True):
        """Fade Out
            Parameters:
            duration (float): duration of animation in seconds
            blocking (bool): whether this animation should stop other animations until its done
       """
        if starting_time == "not_set":
            starting_time = self.lastAnimationTime;
        startingFrame, lastFrame = self.get_anim_frames(duration, starting_time);
        starting_color = self.running_positions["color"]

        for i in range(startingFrame, lastFrame+1):
            alpha = 1-self.get_prog(i, startingFrame, lastFrame)
            starting_color.a = alpha;
            self.insert_animation_into_frame(self.anim_set_color, [Color(starting_color.r, starting_color.g, starting_color.b, starting_color.a)], i ); 

        self.running_positions["color"] = starting_color;
        if blocking:
            self.lastAnimationTime = starting_time + duration;
        return self

    def fade_in(self, duration=0.5, starting_time="not_set", blocking=True):
        if starting_time == "not_set":
            starting_time = self.lastAnimationTime;
        startingFrame, lastFrame = self.get_anim_frames(duration, starting_time);
        starting_color = self.running_positions["color"]

        for i in range(startingFrame, lastFrame+1):
            alpha = self.get_prog(i, startingFrame, lastFrame)
            starting_color.a = alpha
            self.insert_animation_into_frame(self.anim_set_color, [Color(starting_color.r, starting_color.g, starting_color.b, starting_color.a)], i ); 

        self.running_positions["color"] = starting_color;
        if blocking:
            self.lastAnimationTime = starting_time + duration;
        return self

    def rotate(self, angle, duration=0.5, starting_time="not_set", blocking=True, around="not_set", pi_mode=False):
           """Rotate
            Parameters:
            angle (float): the angle to rotate, either in degrees or radians set by pi mode.
            duration (float): duration of animation in seconds
            blocking (bool): whether this animation should stop other animations until its done
            around (Point): a point to rotate around, default is the center of the object
            pi_mode (bool): whetor the angle is in degrees or radians
           """
        if not pi_mode:
            angle = (angle /180)*math.pi;
        self.recalculate_position_from_points()
        #print(f"around: {around.x} {around.y}, self: {self.x} {self.y}");

        if starting_time == "not_set":
            starting_time = self.lastAnimationTime;
        starting_frame, last_frame = self.get_anim_frames(duration, starting_time);

        subAngle = angle/(last_frame-starting_frame+1);
        for i in range(starting_frame, last_frame+1):
            self.insert_animation_into_frame( self.rotate_object_by_angle, [subAngle, around], i);

        self.insert_animation_into_frame( self.recalculate_position_from_points, [], last_frame);
        if blocking:
            self.lastAnimationTime = starting_time + duration;
        return self;

    def wait(self, duration=0.5):
       """Makes object wait
        Parameters:
        duration (float): duration of animation in seconds
       """
        self.lastAnimationTime = self.lastAnimationTime + duration;
        return self
    """ Averages out new x y coordinates from the points, used inorder to fix irregualar shapes and wonky rotations """
    def recalculate_position_from_points(self):
        newx = 0
        newy = 0
        counter = 0
        for point in self.points:
            newx += point.x
            newy += point.y
            counter+= 1

        self.x = newx/counter
        self.y = newy/counter

    """ Helper functio used during rendering of animation """
    def rotate_object_by_angle(self, angle, around="not_set"):
        if around == "not_set":
            around = Point(self.x, self.y);
        for i, point in enumerate(self.points):
            self.points[i] =  BasicObject.rotate_point_by_angle(point, angle, around);

    def rotate_point_by_angle(point, angle, around):
        point = Point(point.x - around.x, point.y - around.y) # change the orgin so we rotate around ourselves instead of the real origin
        newx =  around.x + (point.x*math.cos(angle)- point.y*math.sin(angle));
        newy =  around.y + (point.y*math.cos(angle) + point.x*math.sin(angle));
        #print(f"new x: {newx} y: {newy} angle: {angle} cos: {math.cos(angle)} px {point.x} py {point.y}");
        return Point(newx, newy);


def lin_interpolate(x1, y1, x2, y2, x3):
    return y1 + (x3 - x1) * ((y2-y1)/(x2-x1))

class Shape(BasicObject):

    def translate(self, x=0, y=0, duration=0.5, starting_time="not_set"):
       """Translate
        Parameters:
        duration (float): duration of animation in seconds
        x (int): how much to translate in the x direction
        y (int):  how much to translate in the y direction
       """
        self.move_to(Point(self.running_positions["x"] + x, self.running_positions["y"] + y), duration=duration, starting_time=starting_time);
        return self

    def set_color(self, color, duration=0.5, starting_time="not_set", blocking=True):
       """Set color
        Parameters:
        color (color): the color to turn too
        duration (float): duration of animation in seconds
        blocking (bool): whether this animation should stop other animations until its done
       """
        if starting_time == "not_set":
            starting_time = self.lastAnimationTime

        startingFrame, lastFrame = self.get_anim_frames(duration, starting_time);
        starting_color = self.running_positions["color"];
        for i in range(startingFrame, lastFrame+1):
            self.insert_animation_into_frame(self.lerp_to_color, [color, startingFrame, lastFrame, i, starting_color], i ); 

        self.running_positions["color"] = color;

        if blocking:
            self.lastAnimationTime = starting_time + duration

        return self

    def move_to(self, point, duration=0.5, starting_time="not_set"):
       """Move to 
        Parameters:
        point (Point): the location to move to (should be a point such as Point(x=0,y=0)
        duration (float): duration of animation in seconds
       """
        self.running_positions["x"] = point.x;
        self.running_positions["y"] = point.y;

        if starting_time == "not_set":
            starting_time = self.lastAnimationTime
        startingFrame, lastFrame = self.get_anim_frames(duration, starting_time);
        for i in range(startingFrame, lastFrame+1):
            self.insert_animation_into_frame(self.lerp_to, [point, startingFrame, lastFrame,i, BasicObject.animationIdCount], i ); 

        BasicObject.animationIdCount += 1;
        self.lastAnimationTime = starting_time+duration;
        return self

    def lerp_to_color(self, color, first_frame, last_frame, current_frame_index, starting_color):

        lerped_r = lin_interpolate(first_frame, starting_color.r, last_frame, color.r, current_frame_index) ## we dont want current position, we want intial posisiton 
        lerped_g = lin_interpolate(first_frame, starting_color.g, last_frame, color.g, current_frame_index) ## we dont want current position, we want intial posisiton 
        lerped_b = lin_interpolate(first_frame, starting_color.b, last_frame, color.b, current_frame_index) ## we dont want current position, we want intial posisiton 

        self.color = Color.RGB(lerped_r, lerped_g, lerped_b);

    def lerp_to(self, final_point, first_frame, last_frame, current_frame_index, animation_id):
        starting_x = 0;
        starting_y = 0;

        #print(f" last {last_frame} current : {current_frame_index}") 
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
    def RGB(r,g,b,a=255):
        return Color(r/255, g/255,b/255, a/255);
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

        self.running_positions["x"] = x;
        self.running_positions["y"] = y;

    def calcPoints(self):
        width = self.width
        height = self.height

        return [Point(self.x-width/2,self.y-height/2), Point(self.x+width/2, self.y-height/2), Point(self.x+self.width/2, self.y+self.height/2), Point(self.x-width/2,self.y+self.height/2)]

    def setY(self, y):
        self.y = y;
        self.points = self.calcPoints();

    def setX(self, x):
        self.x = x;
        self.points = self.calcPoints();


