import os
from bot.config import ADB_ADDRESS, SCREENSHOT_PATH

def connect_to_memu():
    os.system(f"adb connect {ADB_ADDRESS}")

def take_screenshot(filename=SCREENSHOT_PATH):
    connect_to_memu()
    os.system(f"adb -s {ADB_ADDRESS} exec-out screencap -p > {filename}")
