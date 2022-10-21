from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(386, 342)[0] == 0:
        click(386, 342)
    if pyautogui.pixel(459 , 342)[0] == 0:
        click(459 , 342)
    if pyautogui.pixel(539 , 342)[0] == 0:
        click(539 , 342)
    if pyautogui.pixel(603 , 342)[0] == 0:
        click(603 , 342)
