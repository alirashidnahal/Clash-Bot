import os

#  آدرس پیش‌فرض MEmu
ADB_ADDRESS = "127.0.0.1:21503"

def connect_to_memu():
    os.system(f"adb connect {ADB_ADDRESS}")

def take_screenshot(filename="screen.png"):
    connect_to_memu()
    os.system(f"adb -s {ADB_ADDRESS} exec-out screencap -p > {filename}")
