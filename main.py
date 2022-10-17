from unittest import skip
from pyautogui import *
import pyautogui as py
import pydirectinput as pyd
import time
import keyboard
import win32api, win32con

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def get_cords():
    x,y = win32api.GetCursorPos()
    print(x,y)

while not keyboard.is_pressed('q'):

    py.moveTo(1152,380)
    click()
    time.sleep(3)

def main():

    start = py.locateCenterOnScreen("Start.png", region=(927,33,959,537), grayscale=True, confidence=0.75)
    begin1 = py.locateCenterOnScreen("Begin.png", region=(927,33,959,537), grayscale=True, confidence=0.75)
    support = py.locateCenterOnScreen("LastOnline.png", region=(927,33,959,537), grayscale=True, confidence=0.75)
    begin2 = py.locateCenterOnScreen("Begin2.png", region=(927,33,959,537), grayscale=True, confidence=0.75)
    skip_story = py.locateCenterOnScreen("Skip.png", region=(927,33,959,537), grayscale=True, confidence=0.75)
    pause_button = py.locateCenterOnScreen("PB.png", region=(927,33,959,537), grayscale=True, confidence=0.75)
    next = py.locateCenterOnScreen("Next.png", region=(927,33,959,537), grayscale=True, confidence=0.75)

    if start is not None:
        py.moveTo(start)
        get_cords()
        time.sleep(2)
        click()
        time.sleep(3)

    if begin1 is not None:
        py.moveTo(begin1)
        get_cords()
        time.sleep(2)
        click()
        time.sleep(2)

    if support is not None:
        py.moveTo(support)
        get_cords()
        time.sleep(2)
        click()
        time.sleep(2)

    if begin2 is not None:
        py.moveTo(begin2)
        get_cords()
        time.sleep(2)
        click()
        time.sleep(2)

    if skip_story is not None:
        py.moveTo(skip_story)
        get_cords()
        time.sleep(2)
        click()
        time.sleep(2)

    if pause_button is not None:
        time.sleep(140)

    if next is not None:
        py.moveTo(next)
        get_cords()
        time.sleep(2)
        click()
        time.sleep(2)
        click()
        time.sleep(2)
        click()
        time.sleep(2)

if __name__ == '__main__':
    main()