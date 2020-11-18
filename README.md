# PYXInput

A Python Library for emulating xbox controllers on Windows as well as reading the state of controllers using standard XInput. This is an adaptation of the the vXbox by vJoy made by user `bayangan1991` [at](https://github.com/bayangan1991/PYXInput) that makes it way more fun to use. The original implementation can be found at [vXboxInterface](http://vjoystick.sourceforge.net/site/index.php/vxbox) but be aware it will not function with the project.
This fork's purpose is to improve upon readability, useability and bling bling.

## Prerequisites

This library should work with anything after Python 3.6, albeit testing has only been done on 3.8.4 and later. 

To use the Virtual Controller object, you need `ScpVBus`. For ease [one of it's versions](https://github.com/shauleiz/vXboxInterface) is included in this project. More information about the original can be found at [nefarius's archived repo](https://github.com/nefarius/ScpVBus).
You'll probably also require [x360ce](https://www.x360ce.com/#Help_Old_Version) for easing the connection to games as well as debugging it. I've included it's older version as that's the one that worked for me. 

### Installing ScpVbus
Open an elevated cmd command prompt in the ScpVBus-x64 directory and run `devcon.exe install ScpVBus.inf Root\ScpVBus`. Successful run is indicated by the following message:

    Device node created. Install is complete when drivers are installed...
    Updating drivers for Root\ScpVBus from {Location}\PYXInput\ScpVBus-x64\ScpVBus.inf.
    Drivers installed successfully.

## Installing
Now that the basics are done, we ought to go throught the usual motions:

### Install via pip

    pip install gamePyd

### Are you in a rush?
Ok, so here goes, this library contains two main modules. [writePad](/gamePyd/writePad.py) is for creating a virtual controller and
[readPad](/gamePyd/readPad.py) is for reading the current state of any xbox controller (virtual or real). Run to line 77 of the former to start controlling.

If you're not in a rush, we've got a bit more to talk about.


### Test the creation of virtual controllers
Running `pyxinput.test_virtual()` should yield:
```
Connecting Controller:
This ID: 1
Available: [2, 3, 4]
Setting TriggerR and AxisLx:
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Done, disconnecting controller.
Available: [1, 2, 3, 4]
```

### Test the reading of controllers
Running `test_read()` should give (the output below was when no controller was plugged-in):


```
Testing controller in position 1:
This will just take a second. We'll look at the controller values in 200 milli-second intervals:
0---------------------------------------------
State:{'LT': 0, 'RT': 0, 'Lx': 0, 'Ly': 0, 'Rx': 0, 'Ry': 0, 'UP': False, 'DOWN': False, 'LEFT': False, 'RIGHT': False, 'START': False, 'SELECT': False, 'L3': False, 'R3': False, 'LB': False, 'RB': False, 'A': False, 'B': False, 'X': False,
 'Y': False}
---------------------------------------------
1---------------------------------------------
State:{'LT': 0, 'RT': 0, 'Lx': 0, 'Ly': 0, 'Rx': 0, 'Ry': 0, 'UP': False, 'DOWN': False, 'LEFT': False, 'RIGHT': False, 'START': False, 'SELECT': False, 'L3': False, 'R3': False, 'LB': False, 'RB': False, 'A': False, 'B': False, 'X': False,
 'Y': False}
---------------------------------------------
2---------------------------------------------
State:{'LT': 0, 'RT': 0, 'Lx': 0, 'Ly': 0, 'Rx': 0, 'Ry': 0, 'UP': False, 'DOWN': False, 'LEFT': False, 'RIGHT': False, 'START': False, 'SELECT': False, 'L3': False, 'R3': False, 'LB': False, 'RB': False, 'A': False, 'B': False, 'X': False,
 'Y': False}
---------------------------------------------
3---------------------------------------------
State:{'LT': 0, 'RT': 0, 'Lx': 0, 'Ly': 0, 'Rx': 0, 'Ry': 0, 'UP': False, 'DOWN': False, 'LEFT': False, 'RIGHT': False, 'START': False, 'SELECT': False, 'L3': False, 'R3': False, 'LB': False, 'RB': False, 'A': False, 'B': False, 'X': False,
 'Y': False}
---------------------------------------------
4---------------------------------------------
State:{'LT': 0, 'RT': 0, 'Lx': 0, 'Ly': 0, 'Rx': 0, 'Ry': 0, 'UP': False, 'DOWN': False, 'LEFT': False, 'RIGHT': False, 'START': False, 'SELECT': False, 'L3': False, 'R3': False, 'LB': False, 'RB': False, 'A': False, 'B': False, 'X': False,
 'Y': False}
---------------------------------------------
Better yet, you can use prettyRead() to sample as many times as desired for any required duration.
And then return it as a dataframe, can even write it to a file by supplying the filename.
    LT  RT  Lx  Ly  Rx  Ry     UP   DOWN   LEFT  RIGHT  START  SELECT     L3     R3     LB     RB      A      B      X      Y             time(ns)  timeDelta(ms)  error(ms)
0   0   0   0   0   0   0  False  False  False  False  False   False  False  False  False  False  False  False  False  False  1605620332292776700         9.9744   1.641067
1   0   0   0   0   0   0  False  False  False  False  False   False  False  False  False  False  False  False  False  False  1605620332301749900         8.9732   0.639867
2   0   0   0   0   0   0  False  False  False  False  False   False  False  False  False  False  False  False  False  False  1605620332310727300         8.9774   0.644067
3   0   0   0   0   0   0  False  False  False  False  False   False  False  False  False  False  False  False  False  False  1605620332319701900         8.9746   0.641267
4   0   0   0   0   0   0  False  False  False  False  False   False  False  False  False  False  False  False  False  False  1605620332328678100         8.9762   0.642867
Do note that the final three columns are metadata.
```

### Coding Styles
I'll be updating the wiki once this project gets to v0.1.0 (see the accompanying project-board for a pseudo-timeline).

## Credits
* **Ayush Rawat** - *Main Developer* - [PCplays](https://github.com/PCplays)

* **Ryan Barnes** - *Authot of PYXInput* - [bayangan1991](https://github.com/bayangan1991)

See also the list of [contributors](https://github.com/bayangan1991/PYXInput/graphs/contributors) who participated in PYXinput (from which this project was forked).

## Acknowledgments

* Everyone at [vJoy](http://vjoystick.sourceforge.net/site/) for the vXboxInterface DLL
* [nefarius](https://github.com/nefarius) for [ScpVBus](https://github.com/nefarius/ScpVBus)
