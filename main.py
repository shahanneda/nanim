import math
import cairo
import utility
from utility import *
import os
import subprocess;

WIDTH, HEIGHT = 1000, 1000
TEMP_FRAMES_LOCATION_NAME = "TEMP-Anim-Frames/"

#objectsToDraw.append(BasicObject([Point(0,0), Point(100,0), Point(100,100), Point(0,100)], Color(0,1,0)))


class Scene:
    FRAME_RATE = 10;
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

    def run_animation(self):
        try:
            os.mkdir(os.path.join(os.path.dirname(__file__), TEMP_FRAMES_LOCATION_NAME));
        except:
            pass;

        print("Rendering Frames");
        for i, frame in enumerate(self.frames):
            for action in frame:
                action[0]( *action[1]) # this is calling that first action, with the arguamets giving in the other one
            self.drawFrame()
            self.writeFrame(i)

        self.make_video_from_frames();

    def make_video_from_frames(self):
        ffmpegCmd = (f"ffmpeg -r {Scene.FRAME_RATE} -f image2 -s 1920x1080 -i ./{TEMP_FRAMES_LOCATION_NAME}%d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p test.mp4 -y").split();
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

rect1 = s.add(Rectangle(0,0,100,100,Color(1,0,0)));

rect1.move_to(Point(1000,1000), duration=2)
rect1.move_to(Point(0,0), duration=3)

"""rect4 = s.add(Rectangle(0,0,100,100, Color(0,0.1,1)))
for i in range(0,25):
    rect4.move_to(Point(250,500), duration=0.5, starting_time=i)
    rect4.move_to(Point(750,500), duration=0.5, starting_time=i+0.5)
"""
'''
rect1.move_to(Point(100,250) , 5, 0)
rect1.move_to(Point(700,250) , 5, 5)
rect1.move_to(Point(800,0), 5, 10)
'''

s.run_animation()


