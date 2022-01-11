# MIT License

# Copyright 2022 Svetlana Ankundinov

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import random
from pynput.mouse import Button
from pynput.keyboard import Key

def rfloatrange(lower : float, upper : float) -> float:
    """Generate a randomized float within the provided range. 

    Args:
        lower (float): Lower bound
        upper (float): Upper bound

    Returns:
        float: Randomized float within the provided range. 
        
    Raises:
        InvalidIntervalError: Raised if the provided interval is invalid.

    """
    if lower > upper:
        raise InvalidIntervalError
    return random.uniform(lower, upper)


def rintrange(lower : int, upper : int) -> int :
    """Generate a randomized integer within the provided range.

    Args:
        lower (int): Lower bound
        upper (int): Upper bound

    Returns:
        int: Randomized integer within the provided range. 
        
    Raises:
        InvalidIntervalError: Raised if the provided interval is invalid.

    """
    if lower > upper:
        raise InvalidIntervalError
    return random.randrange(lower, upper)


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
    """Converts a string to the button representation.

    Args:
        str (str): The string to be converted. 

    Raises:
        InvalidButtonError: Raised if the string passed in is invalid.

    Returns:
        object: Returns the Button object. 
    """
    
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
    """Converts a string to the key representation.

    Args:
        str (str): The string to be converted. 

    Returns:
        Key: Returns the key object or string required by the controller. 
    """
    
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
