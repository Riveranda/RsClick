import unittest
import sys
from pynput.keyboard import Key
from pynput.mouse import Button
import logging as log
  
# setting path
sys.path.append('../RsClick')
  
# importing
from RsClick.TimeLine import *

class TestHelpers(unittest.TestCase):

    def test_range(self):
        fl = rfloatrange(0, 25)
        self.assertIs(type(fl), float)
        self.assertTrue(fl >= 0 and fl <= 25)
        min = rintrange(0, 25)
        self.assertIs(type(min), int)
        self.assertTrue(min >= 0 and min <= 25)

    def test_to_key(self):
        self.assertEqual(strtokey("a"), "a")
        self.assertEqual(strtokey("ctrl"), Key.ctrl)
    
    def test_to_btn(self):
        self.assertEqual(strtobtn("l"), Button.left)
        self.assertEqual(strtobtn("left"), Button.left)
        self.assertEqual(strtobtn("r"), Button.right)
        self.assertEqual(strtobtn("right"), Button.right)

class TestMouse(unittest.TestCase):

    def test_doubleclick(self):
        MouseClickEvent("l", doubleclick=True).execute()

    
    def test_hold(self):
        MouseClickEvent("l", hold=.5).execute()

    
    def test_releasedelay(self):
        MouseClickEvent("l", releasedelay=[.3, .8]).execute()

    
    def test_mouse_move(self):
        MouseMoveEvent(500,500).execute()

    
    def test_mouse_move_invalid(self):
        MouseMoveEvent(-100000,-100000).execute()
        MouseMoveEvent(100000,100000).execute()

    def test_mouse_move_relative(self):
        MouseMoveEvent(100,-500, relative=True).execute()

    def test_mouse_scroll(self):
        MouseScrollEvent(2).execute()

    def test_invalid_button_exception(self):
        with self.assertRaises(InvalidButtonError):
            MouseClickEvent("g").execute()
    
    def test_invalid_interval_exception(self):
        with self.assertRaises(InvalidIntervalError):
            MouseClickEvent("l", releasedelay=[5, 3]).execute()
        with self.assertRaises(InvalidIntervalError):
            MouseClickEvent("l", releasedelay=[3]).execute()
        
class TestPauseEvent(unittest.TestCase):

    def test_pause_int(self):
        PauseEvent(.1).execute()
    
    def test_pause_range(self):
        PauseEvent([.1, .2]).execute()
class TestKeyboard(unittest.TestCase):

    def test_key_press(self):
        KeyEvent("a").execute()

    def test_key_press_hold(self):
        KeyEvent("a", hold=.1).execute()

    def test_key_press_release_delay(self):
        KeyEvent("a", releasedelay=[.1, .2]).execute()
        with self.assertRaises(InvalidIntervalError):
            MouseClickEvent("l", releasedelay=[5, 3]).execute()
        with self.assertRaises(InvalidIntervalError):
            MouseClickEvent("l", releasedelay=[3]).execute()

if __name__ == '__main__':
    log.warning("WARNING: THESE TESTS WILL MOVE YOUR MOUSE AND INPUT KEYS TO TEST FUNCTIONALITY")
    unittest.main()
