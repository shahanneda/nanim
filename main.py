import math
import cairo
import utility
from utility import *

WIDTH, HEIGHT = 256, 256

objectsToDraw = []
objectsToDraw.append(BasicObject([Point(0,0), Point(100,0), Point(100,100), Point(0,100) ]));

objectsToDraw.append(Rectangle(200,200,20,20, color=Color.))

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(0.8, 0.8, 1)
ctx.fill()

for object in objectsToDraw:
    ctx.move_to(object.points[0].x, object.points[0].y)

    for point in object.points[1:]: # skip first point since we already moved there
        ctx.line_to(point.x, point.y)
    ctx.close_path()


ctx.set_source_rgb(1, 0, 0)
ctx.fill()




#ctx.rectangle(0, 0, 50, 120)
#ctx.set_source_rgb(1, 0, 0)
#ctx.fill()

surface.write_to_png("example.png")



