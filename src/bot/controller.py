import os
from bot.adb_tools import ADB_ADDRESS, connect_to_memu

def tap_on_point(x, y):
    connect_to_memu()
    os.system(f"adb -s {ADB_ADDRESS} shell input tap {x} {y}")
