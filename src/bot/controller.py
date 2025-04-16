import os

def tap_on_point(x, y):
    os.system(f"adb shell input tap {x} {y}")
