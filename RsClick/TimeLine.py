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

import logging as log
from pynput.mouse import Controller as mctrl
from pynput.keyboard import  Controller as kctrl
from .utils import *


MOUSE_CONTROLLER = mctrl()
KEYBOARD_CONTROLLER = kctrl()

class TimeLine:
    """TimeLine responsible for storing and executing events. 

    Args:
        startpause (float, optional): Time to pause before executing the script. Defaults to 5.0.
        verbose (bool, optional): Print out event happenings. Defaults to True.
        repeat (bool, optional): Repeat the script indefinitely. Defaults to True.
        defaultEventPause (float, optional): Default time to pause between events. If left unset, there will be no delay. Defaults to 0.0.
    """


    def __init__(self, *events, startpause : float = 5.0, verbose : bool = True, repeat : bool = True, defaultEventPause : float = 0.0):
        self.events = events
        self.startpause = startpause
        self.verbose = verbose
        self.repeat = repeat
        self.defaulteventpause = PauseEvent(defaultEventPause)
        self.ERROR = None


    def start(self):
        """Begins the consecutive execution of events. 

        Raises:
            InvalidEventError: Raised if an invalid object is passed into the TimeLine.
        """
        try:
            PauseEvent(self.startpause).execute(verbose=True)
            while True:
                for event in self.events:
                    if not isinstance(event, Event):
                        raise InvalidEventError
                    event.execute(verbose=self.verbose)
                    if self.defaulteventpause.getTime != 0:
                        self.defaulteventpause.execute()
                if not self.repeat:
                    break
        except Exception as e:
            self.ERROR = e
            log.error(f"An error has occured.{e}")


    def setDefaultEventPause(self, time : float):
        self.defaulteventpause = PauseEvent(time)

class Event:
    """Base Event class
    """
    def execute(self):
        pass

class PauseEvent(Event):
    """Pause event. Pause the script. 

    Args:
        time (object): float or a list of floats of length 2 representing a randomization range. 
    """    

    def __init__(self, time : object):

        self.time = time


    def execute(self, verbose : bool = False):
        """Execute the configured Event

        Args:
            verbose (bool, optional): Print out event occurances. Defaults to False.
        """
        import time
        if verbose:
            log.info(f"Sleeping for {self.time} seconds!")
        if type(self.time) == list:
            time.sleep(rfloatrange(self.time[0], self.time[1]))
        else:
            time.sleep(self.time)    


    def getTime(self) -> float:
        return self.time

class MouseClickEvent(Event):
    """A Mouse click event. 

    Args:
        button (str): "l", "r", "left", or "right".
        releasedelay (list, optional): Range for which to calculate the release delay.. Defaults to [.0824, .223].
        doubleclick (bool, optional): Doubleclick. Defaults to False.
        hold (float, optional): How long to hold the button down. Defaults to 0.0.
    """
    
    def __init__(self, button : str, releasedelay = [.0824, .223], doubleclick = False, hold : float = 0.0):
        self.button = strtobtn(button)
        self.releasedelay = releasedelay
        self.doubleclick = doubleclick
        self.hold = hold
    

    def execute(self, verbose : bool = False):
        """Execute the configured event. 

        Args:
            verbose (bool, optional): Print out event occurances. Defaults to False.

        Raises:
            InvalidIntervalError: Raised if an invalid interval is passed.
        """
        
        if(self.doubleclick):
            MOUSE_CONTROLLER.click(self.button, 2)
            if verbose:
                log.info("Mouse doubleclicked")
        else:
            if verbose:
                log.info("Mouse clicked")
            MOUSE_CONTROLLER.press(self.button)
            if(self.hold == 0.0):
                if len(self.releasedelay) != 2 or self.releasedelay[0] > self.releasedelay[1]:
                    log.error("An InvalidIntervalError has been raised in MouseClickEvent.execute()")
                    raise InvalidIntervalError
                if verbose:
                    log.info(f"Holding for {self.hold} seconds.")
                PauseEvent(self.releasedelay).execute()
            else:
                PauseEvent(self.hold).execute()
            if verbose:
                    log.info("Mouse released.")
            MOUSE_CONTROLLER.release(self.button)


class MouseMoveEvent(Event):
    """A Mouse movement event. 

    Args:
        x (int): The x coordinate to move to.
        y (int): The y coordinate to move to.
        relative (bool, optional): Move the mouse relative to the current position. Defaults to False.
    """    


    def __init__(self, x : int, y: int, relative : bool = False):
        self.x = x
        self.y = y
        self.relative = relative


    def execute(self, verbose : bool = False):
        """Execute the configured event.

        Args:
            verbose (bool, optional): Print out event occurances.. Defaults to False.
        """
        
        if(self.relative):
            if verbose:
                log.info(f"Mouse moved to ({self.x}, {self.y})")
            MOUSE_CONTROLLER.move(self.x, self.y)
        else:
            if verbose:
                log.info(f"Mouse moved by ({self.x}, {self.y}) relative to your previous position.")
            MOUSE_CONTROLLER.position = (self.x, self.y)


class KeyEvent(Event):
    """A Keypress Event
   
    Args:
            key (str): String representation of the desired key. 
            releasedelay (list, optional): A list of 2 floats defining the randomization range. Defaults to [.0824, .223].
            hold (float, optional): Float representating how long to hold the key down. Defaults to 0.0.
    """


    def __init__(self, key : str, releasedelay = [.0824, .223], hold : float = 0.0) -> None:
        self.key = strtokey(key)
        self.releasedelay = releasedelay
        self.hold = hold
    

    def execute(self, verbose : bool = False):
        """Execute the configured event. 

        Args:
            verbose (bool, optional): Print out event occurances. Defaults to False.

        Raises:
            InvalidIntervalError: Raised if an invalid interval is provided. 
        """
        if verbose:
            log.info(f"Key {self.key} pressed")
        KEYBOARD_CONTROLLER.press(self.key)
        if(self.hold == 0.0):
            if len(self.releasedelay) != 2 or self.releasedelay[0] > self.releasedelay[1]:
                log.error("An InvalidIntervalError has been raised in KeyEvent.Execute()")
                raise InvalidIntervalError
            if verbose:
                log.info(f"Holding for {self.hold} seconds.")
            PauseEvent(self.releasedelay).execute()
            if verbose:
                log.info("Key released.")
        else:
            PauseEvent(self.hold).execute()
        KEYBOARD_CONTROLLER.release(self.key)

class TypeEvent(Event):
    """A string typing event. 
    
    Args:
        str (str): The string you wish typed. 
    """


    def __init__(self, str : str):
        self.str = str
    
    def execute(self, verbose : bool = False):
        """Execute the configured event. 

        Args:
            verbose (bool, optional): Print out event occurances. Defaults to False.
        """
        
        if verbose:
            log.info(f"Typing message: {self.str}")
        KEYBOARD_CONTROLLER.type(self.str)

class MouseScrollEvent(Event):
    """A mouse scrolling event.

    Args:
        delta (int): How far to scroll the wheel. 
    """
    
    def __init__(self, delta : int):

        self.delta = delta

    
    def execute(self, verbose : bool = False):
        """Execute the configured event. 

        Args:
            verbose (bool, optional): Print out event occurances. Defaults to False.
        """
        if verbose:
            log.info(f"Mouse scrolled by {self.delta}")
        MOUSE_CONTROLLER.scroll(0 , self.delta)

        
