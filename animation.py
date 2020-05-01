from nanim import *; 

s = Scene(frame_rate=10, quality=20);




rect = s.add(Rectangle(500,500,100,100, Color.RGB(256,100,90)));
rect.rotate(360*10, duration=10, around=Point(500,500)).fadeOut();

s.add(Rectangle(x=500, y=200, width=100, height=100, color=Color.RGB(255,0,0)))\
        .fadeIn()\
        .set_color(Color(0,255,0))\
        .wait(2)\
        .set_color(Color(0,0,255))\
        .wait(3)\
        .fadeOut()\
        .fadeIn(duration=5)\
        .wait(2)\
        .set_color(Color(255, 0,0))\

    
s.add(Rectangle(x=100, y=900, width=50,height=50, color=Color.RGB(60,255,234)))\
        .fadeIn()\
        .translate(x=800, duration=3)\
        .translate(y=-100, x=0)\
        .rotate(360)\
        .translate(y=100, x=0)\
        .rotate(360)\
        .translate(x=-600, duration=3)\
        .rotate(360*10, duration=5, around=Point(500,500))\
        .fadeOut()\
        
s.add(Rectangle(x=500, y=500, width=75, height=100, color=Color.RGB(55,55,255)))\
        .fadeIn()\
        .translate(y=100)\
        .rotate(360*10, around=Point(500,500), duration=10)\
        .fadeOut()\

s.run_animation();
