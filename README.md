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

### Installing x360ce
Extract the provided zip to where your game's executable is.

## Installing
Now that the basics are done, we ought to go throught the usual motions:

### Install via pip

    pip install PYXInput

### Are you in a rush?
Ok, so here goes, this library contains two main modules. [virtual_controller](/pyxinput/virtual_controller.py) is for creating a virtual controller and
[read_state](/pyxinput//read_state.py) is for reading the current state of any xbox controller (virtual or real). Run to line 77 of the former to start controlling.

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
Running `pyxinput.test_read()` should give:

```
Testing controller in position 1:
Running 3 x 3 seconds tests
State:  {'wButtons': 0, 'left_trigger': 0, 'right_trigger': 0, 'thumb_lx': 0, 'thumb_ly': 0, 'thumb_rx': 0, 'thumb_ry': 0}
Buttons:  []
State:  {'wButtons': 0, 'left_trigger': 0, 'right_trigger': 0, 'thumb_lx': 0, 'thumb_ly': 0, 'thumb_rx': 0, 'thumb_ry': 0}
Buttons:  []
State:  {'wButtons': 0, 'left_trigger': 0, 'right_trigger': 0, 'thumb_lx': 0, 'thumb_ly': 0, 'thumb_rx': 0, 'thumb_ry': 0}
Buttons:  []
```

### Coding Styles

Each use case of this library can be initialised as an object. Below is an example of how to use this package.

```python
import pyxinput

MyVirtual = pyxinput.vController()

MyRead = pyxinput.rController(1) # For Controller 1

MyVirtual.set_value('BtnA', 1)
MyVirtual.set_value('AxisLx', -0.5)

print(MyRead.gamepad)
print(MyRead.buttons)
```

## Credits

* **Ryan Barnes** - *Main Developer* - [bayangan1991](https://github.com/bayangan1991)

See also the list of [contributors](https://github.com/bayangan1991/PYXInput/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License

## Acknowledgments

* Everyone at [vJoy](http://vjoystick.sourceforge.net/site/) for the vXboxInterface DLL
* [Sentdex](https://github.com/Sentdex) for the inspiration with his [pygta5](https://github.com/Sentdex/pygta5) project
* [nefarius](https://github.com/nefarius) for [ScpVBus](https://github.com/nefarius/ScpVBus)

