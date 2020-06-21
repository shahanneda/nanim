
# Nanim

An animation library designed from the ground up for a intuitive and easy to use interface. Made in python.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nanim.

```bash
pip install nanim
```
The dependenices are pycairo and ffmpeg, which pip should install automatically.

## Usage
Firstly make an animation file, in which build your animation,

### Sample animation file
```python
s = Scene();
rect = s.add(Rectange(x=0,y=0,width=100,height=100, color=Color.RGB(255,0,0)));
rect.fadeIn().move_to(x=100, y=100).wait(3).fade_out()

s.run_animation();
```

### To render your animation:
- run with `nanim <file-name>` for example `nanim animation.py` where file name is the file name of your animation file
- running `nanim -h` will give you a list of options

### List of all functions callable on objects
```python3
   """Fade Out
    Parameters:
    duration (float): duration of animation in seconds
    blocking (bool): whether this animation should stop other animations until its done
   """
    def fade_out(duration=0.5, blocking=True):
    
   """Fade In
    Parameters:
    duration (float): duration of animation in seconds
    blocking (bool): whether this animation should stop other animations until its done
   """
    def fade_in(duration=0.5, starting_time="not_set", blocking=True):
   
   
   """Rotate
    Parameters:
    angle (float): the angle to rotate, either in degrees or radians set by pi mode.
    duration (float): duration of animation in seconds
    blocking (bool): whether this animation should stop other animations until its done
    around (Point): a point to rotate around, default is the center of the object
    pi_mode (bool): whetor the angle is in degrees or radians
   """
    def rotate(angle, duration=0.5, blocking=True, around="not_set", pi_mode=False):
    
   """Makes object wait
   Parameters:
    duration (float): duration of animation in seconds
   """
    def wait(duration=0.5):
    
   """Translate
    Parameters:
    duration (float): duration of animation in seconds
    x (int): how much to translate in the x direction
    y (int):  how much to translate in the y direction
   """
    def translate(self, x=0, y=0, duration=0.5"):
    
   """Set color
    Parameters:
    color (color): the color to turn too
    duration (float): duration of animation in seconds
    blocking (bool): whether this animation should stop other animations until its done
   """
    def set_color(self, color, duration=0.5, blocking=True):
    
   """Move to 
    Parameters:
    point (Point): the location to move to (should be a point such as Point(x=0,y=0)
    duration (float): duration of animation in seconds
   """
    def move_to(point, duration=0.5):




```


## Contributing
Pull requests are welcome. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
