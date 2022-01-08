# Welcome to RsClick!

Hi! Welcome to RsClick, a brand new method of automating tasks with Python. RsClick is an framework built on top of pynput which allows you to easily create mouse and keyboard macros; allowing you to automate redundant tasks. 

## A brief overview
The primary object you should be familiar with is the TimeLine object. This object is responsible for storing all of your events and executing them. 
The secondary objects are Event objects, which are responsible for holding the information pertaining to each specific event. There are currently five primary events which you may use to construct your script: MouseClickEvent, MouseMoveEvent, KeyEvent, TypeEvent, and PauseEvent. 

## Constructing a script
A script may be constructed by initializing a new TimeLine object and filling its constructor with configured Event objects. The script may then be ran by calling .start() on the TimeLine object.  
```
def main():
	TimeLine(
	PauseEvent(5.6),
	MouseClickEvent("l"),
	MouseMoveEvent(50, -30, relative=True)
	).start()
```

This script when ran will pause for 5.6 seconds, click the left mouse button, and then move the mouse +50x and -30y relative to its current position. 

### MouseClickEvent  
**Usage:**  
MouseClickEvent(button : str)  
**Parameters:**  
*button:* (String) The button you wish to press. Options are: "l", "left", "r", and "right".  
*releasedelay:* (List(Float, Float)). Represents the time in seconds between the button being pressed and released. By default a random float between. 0824 and .223 will be generated. You may override this, and provide a new range for which this value to be calculated.  
*doubleclick:*(Bool) Default is False. If overriden to True it will double click.  
*hold:* (Float) How long you wish the button to be held down for. Please note if this value is set it will override the releasedelay randomization range.  
### MouseMoveEvent  
Please be aware this will instantly move the mouse, and if you are trying to avoid bot detection this is an absolutely terrible idea.  
**Usage**  
MouseMoveEvent(x, y)  
**Parameters**  
*x:* (Int) The x value of the screen to move the mouse to.  
*y:* (Int) The y value of the screen to move the mouse to.  
*relative:* (Bool) Defaulted to false. If overriden to true the mouse will be moved by x and y relative to the current position.  
### KeyEvent  
**Usage**  
KeyEvent(key)  
**Parameters**  
*key:* (Str) The string representation of the key which you wish to press. "a", "esc", "enter", "alt" etc.  
*releasedelay:* (Float) See above under MouseClickEvent.  
*hold:* (Float) See above under MouseClickEvent.  
### TypeEvent  
**Usage**  
TypeEvent("Message")  
**Parameters**  
*str:* (Str) The string you wish typed.   
### PauseEvent  
Time in seconds to pause execution.  
**Usage**  
PauseEvent(5.6)  
**Parameters**  
*time:* (Float) Time in seconds.



