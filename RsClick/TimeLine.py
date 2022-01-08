import time
import random
from pynput.mouse import Button, Controller as mctrl
from pynput.keyboard import Key, Controller as kctrl


MOUSE_CONTROLLER = mctrl()
KEYBOARD_CONTROLLER = kctrl()


class InvalidIntervalError(Exception):
    """Exception raised in the event the alpha value of a time interval is less than the beta value."""


    def __init__(self):
        self.message = "First value must be less than second value for a time range."
        super().__init__(self.message)
        

class InvanlidButtonError(Exception):
    """Exception raised when there is an invalid button"""


    def __init__(self):
        self.message = "Invalid button, options are \"l\" \"left\" \"r\" or \"right\""
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
        raise InvanlidButtonError()
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


def rfloatrange(a : float, b : float) -> float:
    return random.uniform(a, b)


def rintrange(a : int, b : int) -> int :
    return random.randrange(a, b)

class PauseEvent:
    

    def __init__(self, time : object) -> None:
        self.time = time


    def execute(self, verbose : bool):
        if verbose:
            print(f"Sleeping for {self.time} seconds!")
        if type(self.time) == list:
            time.sleep(rfloatrange(self.time[0], self.time[1]))
        else:
            time.sleep(self.time)    

    def getTime(self) -> float:
        return self.time


class TimeLine:
    """Respsonsible for storing and executing events. """


    def __init__(self, *events, startpause : float = 5.0, verbose = True, repeat=True, defaultEventPause = 0.0) -> None:
        self.events = events
        self.startpause = startpause
        self.verbose = verbose
        self.repeat = repeat
        self.defaulteventpause = PauseEvent(defaultEventPause)


    def start(self):
        PauseEvent(self.startpause).execute(True)
        while True:
            for event in self.events:
                event.execute(self.verbose)
                if self.defaulteventpause.getTime != 0:
                    self.defaulteventpause.execute()
            if not self.repeat:
                break


    def setDefaultEventPause(self, time : float):
        self.defaulteventpause = PauseEvent(time)




class MouseClickEvent:


    def __init__(self, button : str, releasedelay = [.0824, .223], doubleclick = False, hold : float = 0.0) -> None:
        self.button = strtobtn(button)
        self.releasedelay = releasedelay
        self.doubleclick = doubleclick
        self.hold = hold
    

    def execute(self, verbose : bool):
        if(self.doubleclick):
            MOUSE_CONTROLLER.click(self.button, 2)
            if verbose:
                print("Mouse doubleclicked")
        else:
            if verbose:
                print("Mouse clicked")
            MOUSE_CONTROLLER.press(self.button)
            if(self.hold == 0.0):
                if verbose:
                    print(f"Holding for {self.hold} seconds.")
                PauseEvent(self.releasedelay).execute(False)
                if verbose:
                    print("Mouse released.")
            else:
                PauseEvent(self.hold).execute(False)
            MOUSE_CONTROLLER.release(self.button)

class MouseMoveEvent:


    def __init__(self, x : int, y: int, relative = False) -> None:
        self.x = x
        self.y = y
        self.relative = relative


    def execute(self, verbose):
        if(self.relative):
            if verbose:
                print(f"Mouse moved to ({self.x}, {self.y})")
            MOUSE_CONTROLLER.move(self.x, self.y)
        else:
            if verbose:
                print(f"Mouse moved by ({self.x}, {self.y}) relative to your previous position.")
            MOUSE_CONTROLLER.position = (self.x, self.y)


class KeyEvent:


    def __init__(self, key : str, releasedelay = [.0824, .223], hold : float = 0.0) -> None:
        self.key = strtokey(key)
        self.releasedelay = releasedelay
        self.hold = hold
    

    def execute(self, verbose : bool):
        if verbose:
            print(f"Key {self.key} pressed")
            KEYBOARD_CONTROLLER.press(self.key)
            if(self.hold == 0.0):
                if verbose:
                    print(f"Holding for {self.hold} seconds.")
                PauseEvent(self.releasedelay).execute(False)
                if verbose:
                    print("Key released.")
            else:
                PauseEvent(self.hold).execute(False)
            MOUSE_CONTROLLER.release(self.key)


class TypeEvent:


    def __init__(self, str : str) -> None:
        self.str = str
    

    def execute(self, verbose : bool):
        if verbose:
            print(f"Typing message: {self.str}")
            KEYBOARD_CONTROLLER.type(self.str)

        
