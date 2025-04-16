import os

def take_screenshot(filename="screen.png"):
    os.system("adb exec-out screencap -p > " + filename)
