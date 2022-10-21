from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#tile 1 X:  421 Y:  367 RGB: ( 16,  20,  19)
#tile 2 X:  491 Y:  363 RGB: (187, 160, 210)
#tile 3 X:  565 Y:  362 RGB: (180, 169, 222)
#tile 4 X:  634 Y:  358 RGB: (179, 179, 231)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#time.sleep(2)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(421, 599) [0] == 16:
        click(421, 599)
    if pyautogui.pixel(491, 599) [0] == 16:
        click(491, 599)
    if pyautogui.pixel(565, 599) [0] == 16:
        click(565, 599)
    if pyautogui.pixel(634, 599) [0] == 16:
        click(634, 599)
    if pyautogui.pixel(421, 599) [0] == 0:
        click(421, 599)
    if pyautogui.pixel(491, 599) [0] == 0:
        click(491, 599)
    if pyautogui.pixel(565, 599) [0] == 0:
        click(565, 599)
    if pyautogui.pixel(634, 599) [0] == 0:
        click(634, 599)
