
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
```python


```


## Contributing
Pull requests are welcome. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
