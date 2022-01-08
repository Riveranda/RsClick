import time
import logging as log
from pynput.mouse import Controller as mctrl
from pynput.keyboard import  Controller as kctrl
from .utils import *

MOUSE_CONTROLLER = mctrl()
KEYBOARD_CONTROLLER = kctrl()

class TimeLine:
    """Responsible for storing and executing events. """


    def __init__(self, *events, startpause : float = 5.0, verbose = True, repeat=True, defaultEventPause = 0.0) -> None:
        self.events = events
        self.startpause = startpause
        self.verbose = verbose
        self.repeat = repeat
        self.defaulteventpause = PauseEvent(defaultEventPause)


    def start(self):
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


    def setDefaultEventPause(self, time : float):
        self.defaulteventpause = PauseEvent(time)
class Event:

    def execute(self):
        pass

class PauseEvent(Event):
    

    def __init__(self, time : object):
        self.time = time


    def execute(self, verbose : bool = False):
        if verbose:
            log.info(f"Sleeping for {self.time} seconds!")
        if type(self.time) == list:
            time.sleep(rfloatrange(self.time[0], self.time[1]))
        else:
            time.sleep(self.time)    

    def getTime(self) -> float:
        return self.time

class MouseClickEvent(Event):


    def __init__(self, button : str, releasedelay = [.0824, .223], doubleclick = False, hold : float = 0.0) -> None:
        self.button = strtobtn(button)
        self.releasedelay = releasedelay
        self.doubleclick = doubleclick
        self.hold = hold
    

    def execute(self, verbose : bool = False):
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


    def __init__(self, x : int, y: int, relative : bool = False):
        self.x = x
        self.y = y
        self.relative = relative


    def execute(self, verbose : bool = False):
        if(self.relative):
            if verbose:
                log.info(f"Mouse moved to ({self.x}, {self.y})")
            MOUSE_CONTROLLER.move(self.x, self.y)
        else:
            if verbose:
                log.info(f"Mouse moved by ({self.x}, {self.y}) relative to your previous position.")
            MOUSE_CONTROLLER.position = (self.x, self.y)

class KeyEvent(Event):


    def __init__(self, key : str, releasedelay = [.0824, .223], hold : float = 0.0) -> None:
        self.key = strtokey(key)
        self.releasedelay = releasedelay
        self.hold = hold
    

    def execute(self, verbose : bool = False):
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


    def __init__(self, str : str):
        self.str = str
    

    def execute(self, verbose : bool = False):
        if verbose:
            log.info(f"Typing message: {self.str}")
        KEYBOARD_CONTROLLER.type(self.str)

class MouseScrollEvent(Event):


    def __init__(self, delta : int):
        self.delta = delta

    
    def execute(self, verbose : bool = False):
        if verbose:
            log.info(f"Mouse scrolled by {self.delta}")
        MOUSE_CONTROLLER.scroll(0 , self.delta)

        
