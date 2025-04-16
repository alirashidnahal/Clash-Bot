import os
from bot.config import ADB_ADDRESS
from bot.adb_tools import connect_to_memu

def tap_on_point(x, y):
    connect_to_memu()
    os.system(f"adb -s {ADB_ADDRESS} shell input tap {x} {y}")
