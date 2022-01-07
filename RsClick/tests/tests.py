import unittest
import sys
from pynput.keyboard import Key
from pynput.mouse import Button
  
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
        exception_was_thrown = False
        try:
            MouseClickEvent("l", doubleclick=True).execute(False)
        except Exception as e: 
            print(e)
            exception_was_thrown = True
        self.assertFalse(exception_was_thrown)
    
    def test_hold(self):
        exception_was_thrown = False
        try:
            MouseClickEvent("l", hold=.5).execute(False)
        except Exception as e:
            print(e)
            exception_was_thrown = True
        self.assertFalse(exception_was_thrown)
    
    def test_releasedelay(self):
        exception_was_thrown = False
        try:
            MouseClickEvent("l", releasedelay=[.3, .8]).execute(False)
        except Exception as e: 
            print(e)
            exception_was_thrown = True
        self.assertFalse(exception_was_thrown)
    
    def test_mouse_move(self):
        exception_was_thrown = False
        try:
            MouseMoveEvent(500,500).execute(False)
        except Exception as e: 
            print(e)
            exception_was_thrown = True
        self.assertFalse(exception_was_thrown)
    
    def test_mouse_move_relative(self):
        exception_was_thrown = False
        try:
            MouseMoveEvent(100,-500, relative=True).execute(False)
        except Exception as e: 
            print(e)
            exception_was_thrown = True
        self.assertFalse(exception_was_thrown)


class TestPauseEvent(unittest.TestCase):

    def test_pause_int(self):
        exception_was_thrown = False
        try:
            PauseEvent(.1).execute(False)
        except Exception as e: 
            print(e)
            exception_was_thrown = True
        self.assertFalse(exception_was_thrown)
    
    def test_pause_range(self):
        exception_was_thrown = False
        try:
            PauseEvent([.1, .2]).execute(False)
        except Exception as e: 
            print(e)
            exception_was_thrown = True
        self.assertFalse(exception_was_thrown)
class TestKeyboard(unittest.TestCase):

    def test_key_press(self):
        exception_was_thrown = False
        try:
            KeyEvent("a").execute(False)
        except Exception as e: 
            print(e)
            exception_was_thrown = True
        self.assertFalse(exception_was_thrown)
    
    def test_key_press_hold(self):
        exception_was_thrown = False
        try:
            KeyEvent("a", hold=.1).execute(False)
        except Exception as e: 
            print(e)
            exception_was_thrown = True
        self.assertFalse(exception_was_thrown)

    def test_key_press_release_delay(self):
        exception_was_thrown = False
        try:
            KeyEvent("a", releasedelay=[.1, .2]).execute(False)
        except Exception as e: 
            print(e)
            exception_was_thrown = True
        self.assertFalse(exception_was_thrown)
    

        

if __name__ == '__main__':
    print("WARNING: THESE TESTS WILL MOVE YOUR MOUSE AND INPUT KEYS TO TEST FUNCTIONALITY")
    unittest.main()
