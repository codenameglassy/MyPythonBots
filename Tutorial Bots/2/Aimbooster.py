from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# region 340,220,650,500
# RGB: (255, 219, 195)

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('e') == False:
    view = pyautogui.screenshot(region=(340,220,650,500))
    width, height = view.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r,g,b = view.getpixel((x,y))
            if b == 195:
                click(x+340,y+220)
                time.sleep(0.05)
                break
