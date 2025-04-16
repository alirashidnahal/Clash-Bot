from bot import adb_tools, analyzer, controller, scheduler
from bot.config import SCREENSHOT_PATH, COLLECTOR_IMAGE_PATH

def run_bot():
    print("[*] Taking SCREENSHOT...")
    adb_tools.take_screenshot()

    print("[*] Searching for full collector...")
    points = analyzer.find_template_on_screen(SCREENSHOT_PATH, COLLECTOR_IMAGE_PATH)

    if points:
        print(f"[+] Found collector at: {points[0]}")
        controller.tap_on_point(*points[0])
    else:
        print("[-] Collector not found on screen.")

if __name__ == "__main__":
    print("[*] Starting bot...")
    scheduler.run_every(interval_minutes=60, job_func=run_bot)
