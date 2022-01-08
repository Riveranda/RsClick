import random
from pynput.mouse import Button
from pynput.keyboard import Key

def rfloatrange(a : float, b : float) -> float:
    return random.uniform(a, b)


def rintrange(a : int, b : int) -> int :
    return random.randrange(a, b)


class InvalidIntervalError(Exception):
    """Exception raised in the event the alpha value of a time interval is less than the beta value."""


    def __init__(self):
        self.message = "First value must be less than second value for a time range."
        super().__init__(self.message)
        

class InvalidButtonError(Exception):
    """Exception raised when there is an invalid button"""


    def __init__(self):
        self.message = "Invalid button, options are \"l\" \"left\" \"r\" or \"right\""
        super().__init__(self.message)

class InvalidEventError(Exception):
    """Exception raised when a class other than an Exception is added to the script"""
        
    def __init__(self) -> None:
        self.message = "Invalid object, objects must be an instance of Event class."
        super().__init__(self.message)


def strtobtn(str : str) -> object:
    str = str.lower().strip().replace(" " , "")
    dict = {
        "l" : Button.left,
        "left" : Button.left,
        "r" : Button.right,
        "right" : Button.right
    }
    if str not in dict:
        raise InvalidButtonError
    return dict[str]


def strtokey(str : str) -> object:
    str = str.lower().strip().replace(" ", "")
    dict = {
        "tab" : Key.tab,
        "alt" : Key.alt,
        "backspace" : Key.backspace,
        "capslock" : Key.caps_lock,
        "command" : Key.cmd,
        "win" : Key.cmd,
        "ctrl" : Key.ctrl,
        "delete" : Key.delete,
        "up": Key.up,
        "left" : Key.left,
        "right" : Key.right,
        "down" : Key.down,
        "end" : Key.end,
        "enter" : Key.enter,
        "esc" : Key.esc,
        "f1" : Key.f1,
        "f2" : Key.f2,
        "f3" : Key.f3, 
        "f4" : Key.f4,
        "f5" : Key.f5,
        "f6" : Key.f6,
        "f7" : Key.f7,
        "f8" : Key.f8,
        "f9" : Key.f9,
        "home" : Key.home,
        "shift" : Key.shift,
        "space" : Key.space,
    }
    return dict[str] if str in dict else str