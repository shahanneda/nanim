import math
import argparse;
import cairo
import utility
import os
import subprocess;
import sys;

from utility import *
WIDTH, HEIGHT = 1000, 1000
TEMP_FRAMES_LOCATION_NAME = "TEMP-Anim-Frames/"

#objectsToDraw.append(BasicObject([Point(0,0), Point(100,0), Point(100,100), Point(0,100)], Color(0,1,0)))


class Scene:
    FRAME_RATE = 10;
    def __init__(self, file_name="animation.mp4", frame_rate=30, quality=20):
        Scene.FRAME_RATE = frame_rate;
        self.objectsToDraw = []
        self.quality = quality 
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
        self.ctx = cairo.Context(self.surface)
        #self.ctx.rotate(3*math.pi/2);
        #self.ctx.translate(WIDTH, -HEIGHT)
        
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

        print("Rendering Frames\n*** ", end="");
        lastprog=0;
        for i, frame in enumerate(self.frames):
            if(lastprog  != self.get_progress(i)):
                lastprog = self.get_progress(i)
                print("-", end="")
                sys.stdout.flush()

            for action in frame:
                action[0]( *action[1]) # this is calling that first action, with the arguamets giving in the other one

            self.drawFrame()
            self.writeFrame(i)

        print(" ***\nDone!\nRendering Video");
        self.make_video_from_frames();

    def get_progress(self, index):
        return abs(round(index*100/len(self.frames)))

    def make_video_from_frames(self):
        ffmpegCmd = (f"ffmpeg -r {Scene.FRAME_RATE} -f image2 -s 1920x1080 -i ./{TEMP_FRAMES_LOCATION_NAME}%d.png -vcodec libx264 -crf {self.quality} -pix_fmt yuv420p test.mp4 -y").split();
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
            self.ctx.set_source_rgba(object.color.r, object.color.g, object.color.b, object.color.a)
            self.ctx.fill()

    def writeFrame(self, index):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, TEMP_FRAMES_LOCATION_NAME  + str(index) + ".png")
        self.surface.write_to_png(filename)



def main():
    # if(len(sys.argv) == 1):
    #     print("ERROR: Enter input filename as first argument!");
    #     return;
    # exec(open(sys.argv[1]).read());
    parser = argparse.ArgumentParser(description='Render a NAnim animation.')
    parser.add_argument("input_filename", help="the file name of the input file");

    parser.add_argument("-f", "--framerate", help="the framerate the animation should be rendered at (in frames per second), the default is 30fps", type=int, default=30)
    parser.add_argument("-q", "--quality", help="the quality of the rendered video file, from 1-100, the default is 50, which is very good quality", type=int, default = 50)

    args = parser.parse_args();
    
    #we need to change to 1-100 to 0-51 for ffmpeg where 0 is gihest quality and 51 is lowest
    real_quality = int( (1-(args.quality/100)) * 51 )
    if real_quality > 51:
        real_quality = 51
    if real_quality < 0:
        real_quality = 0


    print(real_quality);

if __name__ == "__main__":
    main();
"""
rect2 = s.add(Rectangle(x=200, y=200,  width=100, height=100, color=Color.RGB(0.6,0.6,0.6)));
rect2.fadeIn().move_to(Point(200,900), duration=2).fadeIn().fadeOut();

rect5 = s.add(Rectangle(500,500,20,50, Color.RGB(173,0,123)))

rect5.fadeIn(duration=2)\
     .fadeOut()\
     .fadeIn()\
     .move_to(Point(900,200), duration=1)\
     .fadeOut()\
     .move_to(Point(500,500))\
     .fadeIn()\
     .wait(2)\
     .move_to(Point(800, 800))\
     .wait(5)\
     .move_to(Point(200,200))\




rect4 = s.add(Rectangle(0,0,100,100, Color(0,0.1,1)))
for i in range(0,25):
    rect4.move_to(Point(250,500), duration=0.5, starting_time=i)
    rect4.move_to(Point(750,500), duration=0.5, starting_time=i+0.5)
"""
'''
rect1.move_to(Point(100,250) , 5, 0)
rect1.move_to(Point(700,250) , 5, 5)
rect1.move_to(Point(800,0), 5, 10)
'''



