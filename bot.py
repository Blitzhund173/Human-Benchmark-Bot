from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


#Defines the click function
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Hit Q to stop the script
while keyboard.is_pressed('q') == False:
#Checks if pixel 1622, 331 has R value of 75
 if pyautogui.pixel(1622, 331)[0] == 75:
        click(1622, 331)#These coordinates may vary, to find your, open IDLE and paste: "import pyautogui" then "pyautogui.displayMousePosition()". Now hover over the blue area of the test and note the X and Y values of the area and change both values in the code.
