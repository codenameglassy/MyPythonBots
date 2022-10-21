from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import ctypes
import pymsgbox



time.sleep(2)

replayBtnXpos = 792
replayBtnYpos = 662
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Rest mouse
def RestMouse(x,y):
    win32api.SetCursorPos((x,y))

def ClickReplayButton():
    if pyautogui.pixel(replayBtnXpos, replayBtnYpos) [0] == 21:
        click(replayBtnXpos,replayBtnYpos)

 #check if food is max
def CheckIfMaxLevel(): 
    time.sleep(1)
    pic = pyautogui.screenshot(region=(900,220,120,120))
    if pyautogui.locateOnScreen('maxlevel.png', grayscale=True, confidence = 0.9, region=(900,220,120,120)):
        print('max level')
        pymsgbox.alert('This is an alert!', 'Chamipon Max lvl')
    else:
        ClickRepeat()

#click repate button
def ClickRepeat():
    ClickReplayButton()
    time.sleep(2)
    pic_ = pyautogui.screenshot(region=(550,170,250,250))
    if pyautogui.locateOnScreen('energyover.png', grayscale=True, confidence = 0.9, region=(550,170,250,250)):
        print('energy over')
        pymsgbox.alert('This is an alert!', 'Energy Over')
    else:
        time.sleep(1)
        RestMouse(1152, 128)
        time.sleep(1)
   

def MatchFinished():
    if pyautogui.pixel(633,76)[0] == 181:
            time.sleep(3)
            CheckIfMaxLevel()
            
        


#victory screen X:  633 Y:   76 RGB: (181, 162,  82)
#energyover region == 550,170,250,250
#replay button Position X:  792 Y:  662 RGB: ( 21, 124, 156)
#reset mouse button position X: 1152 Y:  128 RGB: ( 31,  26,  25)
#maxlevel region == 900,220,120,120
        
while keyboard.is_pressed('q') == False:
   
    #repeat
    MatchFinished()
    
    
    
   
