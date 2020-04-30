from nanim import *; 

s = Scene();


rect = s.add(Rectangle(500,500,100,100, Color.RGB(256,100,90)));
rect.fadeIn();
rect.rotate(math.pi*2, duration=10);
rect.rotate(math.pi*2, duration=10)\
    .wait(5)\
    .rotate(math.pi/2, duration=5)\
    .rotate(-math.pi/2, duration=5)\

rect1 = s.add(Rectangle(0,0,100,100,Color.RGB(0,70,120)));

rect2 = s.add(Rectangle(500,500,250,250, Color.RGB(10,200,100)))\
    .wait(2)\
    .rotate(math.pi*2, duration=10)

rect1.fadeIn()\
    .fadeOut()\
    .fadeIn()\
    .move_to(Point(500,500), duration=2)\
    .fadeOut()\
    .fadeIn()\
    .fadeOut()\
    .fadeIn()\
    .move_to(Point(1000,1000), duration=2)\
    .move_to(Point(0,0), duration=3)\
    .fadeOut(duration=0.5)\
    .fadeIn()\
    .move_to(Point(100,500))\
    .rotate(angle=math.pi, duration=7, around=rect.get_position())\
    .rotate(angle=-math.pi, duration=5)\
    .rotate(angle=math.pi, duration=7, around=rect.get_position())\

s.run_animation();
