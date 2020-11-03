"""Read the current state of Xbox Controllers"""
from ctypes import *

# Xinput DLL
try:
    _xinput = windll.xinput1_4
except OSError as err:
    _xinput = windll.xinput1_3


class _xinput_gamepad(Structure):
    """CType XInput Gamepad Object"""
    _fields_ = [("wButtons", c_ushort), ("left_trigger", c_ubyte),
                ("right_trigger", c_ubyte), ("thumb_lx", c_short),
                ("thumb_ly", c_short), ("thumb_rx", c_short),
                ("thumb_ry", c_short)]

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

    # All possible button values
    _buttons = {
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
        """Returns the current gamepad state. Buttons pressed is shown as a raw integer value.
        Use rController.buttons for a list of buttons pressed.
        """
        state = _xinput_state()
        _xinput.XInputGetState(self.ControllerID - 1, pointer(state))
        self.dwPacketNumber = state.dwPacketNumber

        return state.XINPUT_GAMEPAD

    @property
    def buttons(self):
        """Returns a list of buttons currently pressed"""
        return [
            name for name, value in rController._buttons.items()
            if (self.read.wButtons & value) == value
        ]


def main():
    """Test the functionality of the rController object"""
    from time import sleep

    print('Testing controller in position 1:')
    print('Running 3 x 3 seconds tests')

    # Initialise Controller
    con = rController(1)

    # Loop printing controller state and buttons held
    for i in range(3):
        print('Waiting...')
        sleep(2.5)
        print('State: ', con.read)
        print('Buttons: ', con.buttons)
        sleep(0.5)
    print('Done!')


if __name__ == '__main__':
    main()
