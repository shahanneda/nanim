import math
import cairo
import utility
from utility import *
import os
import subprocess;
WIDTH, HEIGHT = 1000, 1000
TEMP_FRAMES_LOCATION_NAME = "TEMP-Anim-Frames/"

objectsToDraw = []
#objectsToDraw.append(BasicObject([Point(0,0), Point(100,0), Point(100,100), Point(0,100)], Color(0,1,0)))

objectsToDraw.append(Rectangle(200,200,20,20,Color(0,0.5,0.7) ))

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

def drawFrame():
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.set_source_rgb(0.8, 0.8, 1)
    ctx.fill()

    for object in objectsToDraw:
        ctx.move_to(object.points[0].x, object.points[0].y)

        for point in object.points[1:]: # skip first point since we already moved there
            ctx.line_to(point.x, point.y)
        ctx.close_path()
        ctx.set_source_rgb(object.color.r, object.color.g, object.color.b)
        ctx.fill()

def writeFrame(index):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, TEMP_FRAMES_LOCATION_NAME  + str(index) + ".png")
    surface.write_to_png(filename)


drawFrame();
writeFrame(1);

for i in range(100):
    objectsToDraw[0].setX(objectsToDraw[0].x + 1)
    objectsToDraw[0].color.r += 0.01;
    drawFrame()
    writeFrame(i)

#ctx.rectangle(0, 0, 50, 120)
#ctx.set_source_rgb(1, 0, 0)
#ctx.fill()


ffmpegCmd = ("ffmpeg -r 30 -f image2 -s 1920x1080 -i ./" + TEMP_FRAMES_LOCATION_NAME +"%d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p test.mp4 -y").split();

print(ffmpegCmd);
subprocess.call(ffmpegCmd);
subprocess.call(("rm -rf ./" + TEMP_FRAMES_LOCATION_NAME+ "*").split()); 
subprocess.call("open test.mp4".split());
