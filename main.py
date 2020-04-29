import math
import cairo
import utility
from utility import *
import os
import subprocess;

WIDTH, HEIGHT = 1000, 1000
FRAME_RATE = 10
TEMP_FRAMES_LOCATION_NAME = "TEMP-Anim-Frames/"

#objectsToDraw.append(BasicObject([Point(0,0), Point(100,0), Point(100,100), Point(0,100)], Color(0,1,0)))


class Scene:
    def __init__(self, file_name="animation.mp4"):
        self.objectsToDraw = []
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
        self.ctx = cairo.Context(self.surface)
        self.frames = [];


    def add(self, object):
        if isinstance(object, BasicObject):
            self.objectsToDraw.append(object);
            object.scene = self
        return object;


    def move_object_to(self, object, point, time, starting_time=0):
        startingFrame = starting_time*FRAME_RATE
        totalFrames = startingFrame + time * FRAME_RATE;

        for i in range(int(startingFrame), int(totalFrames)):
            prog = i/int(totalFrames);
            if len(self.frames) > i:
                self.frames[i].append( [ self.change_object_coord, [object, Point(point.x * prog, point.y * prog)]] ); 
            else:
                self.frames.append([ [ self.change_object_coord, [object, Point(point.x * prog, point.y * prog) ] ]  ] ); 

    def change_object_coord(self, object, point):
        object.setX(point.x);
        object.setY(point.y);

    def run_animation(self):
        try:
            os.mkdir(os.path.join(os.path.dirname(__file__), TEMP_FRAMES_LOCATION_NAME));
        except:
            pass;

        for i, frame in enumerate(self.frames):
            for action in frame:
                action[0]( *action[1]) # this is calling that first action, with the arguamets giving in the other one
            self.drawFrame()
            self.writeFrame(i)

        self.make_video_from_frames();

    def make_video_from_frames(self):
        ffmpegCmd = (f"ffmpeg -r {FRAME_RATE} -f image2 -s 1920x1080 -i ./{TEMP_FRAMES_LOCATION_NAME}%d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p test.mp4 -y").split();
        subprocess.call(ffmpegCmd);
        subprocess.call(("rm -rf ./" + TEMP_FRAMES_LOCATION_NAME).split()); 
        subprocess.call("open test.mp4".split());

    def drawFrame(self):
        self.ctx.rectangle(0, 0, WIDTH, HEIGHT)
        self.ctx.set_source_rgb(0.8, 0.8, 1)
        self.ctx.fill()

        for object in self.objectsToDraw:
            self.ctx.move_to(object.points[0].x, object.points[0].y)

            for point in object.points[1:]: # skip first point since we already moved there
                self.ctx.line_to(point.x, point.y)
            self.ctx.close_path()
            self.ctx.set_source_rgb(object.color.r, object.color.g, object.color.b)
            self.ctx.fill()

    def writeFrame(self, index):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, TEMP_FRAMES_LOCATION_NAME  + str(index) + ".png")
        self.surface.write_to_png(filename)

s = Scene();

rectangle1 = Rectangle(0,0,100,100,Color(1,0,0))
s.add(rectangle1)
s.move_object_to(rectangle1, Point(500,100), 5.0)


s.run_animation()


