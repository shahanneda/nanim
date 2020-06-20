#!/usr/bin/env python3
import math
import argparse;
import cairo
import os
import subprocess;
import sys;
from .utility import *;

WIDTH, HEIGHT = 1000, 1000
TEMP_FRAMES_LOCATION_NAME = "TEMP-Anim-Frames/"


class Scene:
    FRAME_RATE = 30;
    QUALITY = 20;
    def __init__(self):
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

        print(f"Rendering Frames: framerate:{Scene.FRAME_RATE} \n*** ", end="");
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
        ffmpegCmd = (f"ffmpeg -r {Scene.FRAME_RATE} -f image2 -s 1920x1080 -i { os.path.join(os.path.dirname(__file__), TEMP_FRAMES_LOCATION_NAME)}%d.png -vcodec libx264 -crf {Scene.QUALITY} -pix_fmt yuv420p {Scene.OUTPUT_FILENAME}.mp4 -y").split();
        subprocess.call(ffmpegCmd);
        subprocess.call(("rm -rf ./" + TEMP_FRAMES_LOCATION_NAME).split()); 
        subprocess.call(f"open {Scene.OUTPUT_FILENAME + '.mp4'}".split());

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

    parser.add_argument("-o", "--output_filename", help="the name of the output file, by default it is output.mp4", default = "output.mp4")
    parser.add_argument("-f", "--framerate", help="the framerate the animation should be rendered at (in frames per second), the default is 30fps", type=int, default=30)
    parser.add_argument("-q", "--quality", help="the quality of the rendered video file, from 1-100, the default is 50, which is very good quality", type=int, default = 50)

    args = parser.parse_args();
    
    #we need to change to 1-100 to 0-51 for ffmpeg where 0 is gihest quality and 51 is lowest
    real_quality = int( (1-(args.quality/100)) * 51 )
    if real_quality > 51:
        real_quality = 51
    if real_quality < 0:
        real_quality = 0

    Scene.OUTPUT_FILENAME= args.output_filename
    if ".mp4" in args.output_filename: # remove extension if user provided it 
        Scene.OUTPUT_FILENAME = "".join(args.output_filename.split(".")[:-1]);



    # open file user specifed
    try:
        file = open(args.input_filename).read()
    except FileNotFoundError:
        print(f"ERROR: FILE NOT FOUND {args.input_filename}");
        return

    #set static scene constants
    Scene.FRAME_RATE = args.framerate
    Scene.QUALITY = real_quality
    # run that file with nanim already imported
    exec(file); 


if __name__ == "__main__":
    main();
