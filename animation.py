from nanim import *; 

s = Scene(frame_rate=10, quality=20);




rect = s.add(Rectangle(500,500,100,100, Color.RGB(256,100,90)));
rect.rotate(360*10, duration=14, pi_mode=False);
    

s.add(Rectangle(500, 600, 200, 200, Color.RGB(0,150, 250)))\
    .fadeIn(duration=2)\
    .rotate(360*10, duration=7, around=Point(500,500))\
    .rotate(-360*10, duration=7, around=Point(500,500))\
    .fadeOut(duration=2)\

s.add(Rectangle(500, 800, 200, 200, Color.RGB(105,150,0 )))\
    .fadeIn(duration=2)\
    .rotate(360*10, duration=7, around=Point(500,500))\
    .rotate(-360.10, duration=7, around=Point(500,501))\
    .fadeOut(duration=2)\

s.add(Rectangle(x=100, y=900, width=50,height=50, color=Color.RGB(60,255,234)))\
        .fadeIn()\
        .translate(x=800, duration=3)\
        .translate(y=-100, x=0)\
        .translate(y=100, x=0)\
        .translate(y=-100, x=0)\
        .translate(y=100, x=0)\
        
s.add(Rectangle(400, 100, 200, 200, Color.RGB(150,0, 250)))\
    .fadeIn(duration=2)\
    .rotate(360*10, duration=7, around=Point(500,500))\
    .rotate(-360*10, duration=7, around=Point(500,500))\
    .fadeOut(duration=2)\


s.run_animation();
