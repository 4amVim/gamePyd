"""Read the current state of Xbox Controllers"""
from ctypes import *
import pandas as pd
from time import time_ns

# Xinput DLL
try:
    _xinput = windll.xinput1_4
except OSError as err:
    _xinput = windll.xinput1_3


class _xinput_gamepad(Structure):
    """CType XInput Gamepad Object"""
    _fields_ = [
        ("wButtons",
         c_ushort),  #Contains all button information in one integer
        ("LT", c_ubyte),  #Left Trigger
        ("RT", c_ubyte),  #Right Trigger
        ("Lx", c_short),  #Right stick horizontal movement
        ("Ly", c_short),  #Right stick vertical movement
        ("Rx", c_short),  #Left stick horizontal movement
        ("Ry", c_short)
    ]  #Left stick vertical movement

    fields = [f[0] for f in _fields_]

    def __dict__(self):
        return {field: self.__getattribute__(field) for field in self.fields}

    def __str__(self):
        return str(self.__dict__())

    def __getitem__(self, string):
        return self.__dict__()[string]


class _xinput_state(Structure):
    """CType XInput State Object"""
    _fields_ = [("dwPacketNumber", c_uint),
                ("XINPUT_GAMEPAD", _xinput_gamepad)]

    fields = fields = [f[0] for f in _fields_]

    def __dict__(self):
        return {field: self.__getattribute__(field) for field in self.fields}

    def __str__(self):
        return str(self.__dict__())

    def __getitem__(self, string):
        return self.__dict__()[string]


class rController(object):
    """XInput Controller State reading object"""

    _buttons = {  # All possible button values
        'UP': 0x0001,
        'DOWN': 0x0002,
        'LEFT': 0x0004,
        'RIGHT': 0x0008,
        'START': 0x0010,
        'SELECT': 0x0020,
        'L3': 0x0040,
        'R3': 0x0080,
        'LB': 0x0100,
        'RB': 0x0200,
        'A': 0x1000,
        'B': 0x2000,
        'X': 0x4000,
        'Y': 0x8000
    }

    def __init__(self, ControllerID):
        """
        Initialise Controller object.
        ControllerID    Int     Position of gamepad.
        """
        self.ControllerID = ControllerID
        self.dwPacketNumber = c_uint()

    @property
    def read(self):
        """
        Returns the current gamepad state.
        """
        state = _xinput_state()
        _xinput.XInputGetState(self.ControllerID - 1, pointer(state))
        self.dwPacketNumber = state.dwPacketNumber
        check = lambda x: (state.XINPUT_GAMEPAD.wButtons & x) == x
        buttons = {
            name: check(value)
            for name, value in rController._buttons.items()
        }
        analogs = state.XINPUT_GAMEPAD.__dict__()
        del analogs['wButtons']
        return {**analogs, **buttons}

    def prettyRead(self, duration=5, rate=float(1 / 120), type="df", file=""):
        """
        Adds more functionality to read
        """
        """
        Opens the game, and records for seconds, possibly writing to file
        seconds=time to record for, in seconds
        interval gives how often to record, in seconds)
        file, if provided, creates/overwrites into that filename at root
        """

        #Setup loop parameters
        line = []
        start = time_ns()
        count = duration // rate
        wait_ns = rate * 10**9
        i = 0

        #Time for the loop
        #pbar = tq(total=count, position=0, leave=True)
        while (i < count):
            #foo=str(xbox.read)
            #jot.write(foo+"\n")
            if (time_ns() >= start + wait_ns):
                moment = self.read  # will return a dictionary for instantaneous state of the controller
                moment['time(ns)'] = time_ns(
                )  #store current time in nanoseconds
                moment['timeDelta(ms)'] = (
                    time_ns() -
                    start) / 10**6  #Store the time diffference in milliseconds
                moment['error(ms)'] = moment['timeDelta(ms)'] - wait_ns / 10**6
                line.append(moment)
                i += 1
                #print(f"time elapsed={((time_ns()-start)/10**6)/1000}")
                start = time_ns()
        #        pbar.update(1)
        #print(f"iteration {i} got gamepad like \n{moment}")
        #else:
        #  i-=1
        #if (debug==True):
        #clear_output(wait=True)  #clears output in jupyter
        #print(f"iteration {i} got gamepad like \n{moment}") #print current state
        #print(f"iteration {i} got line like \n{line}") #print current state
        #sleep(step*0.5)
        #end=perf_counter()
        #dur=end-start
        #print(f"RRRR:-------{dur}") if ((dur)<=step) else print(f"aaaa:>>>>>{dur}")
        #print(f"\n total time={perf_counter()-st}") # print a line to seperate the tqdm progress bar

        #write to disk if wanted
        if (len(file) > 0 and type == "df"):
            (pd.DataFrame(line)).to_feather(file)
        return pd.DataFrame(line)


def main():
    """Test the functionality of the rController object"""
    from time import sleep

    print('Testing controller in position 1:')
    print('Running 3 x 3 seconds tests')

    # Initialise Controller
    con = rController(1)

    # Loop printing controller state and buttons held
    for i in range(5):
        print(f'State:{con.read}')
        print("---------------------------------------------")
        sleep(0.2)
    print(f'State:{con.prettyRead(1)}')
    print(con.prettyRead(1).head)


if __name__ == '__main__':
    main()
