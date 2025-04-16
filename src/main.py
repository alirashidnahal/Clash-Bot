from bot import adb_tools, analyzer, controller, scheduler
from bot.config import SCREENSHOT_PATH, COLLECTOR_IMAGE_PATH

def run_bot():
    print("[*] گرفتن اسکرین‌شات...")
    adb_tools.take_screenshot()

    print("[*] جستجو برای کالکتور پر...")
    points = analyzer.find_template_on_screen(SCREENSHOT_PATH, COLLECTOR_IMAGE_PATH)

    if points:
        print(f"[+] یافت شد در مختصات: {points[0]}")
        controller.tap_on_point(*points[0])
    else:
        print("[-] چیزی پیدا نشد.")

if __name__ == "__main__":
    print("[*] اجرای ربات آغاز شد...")
    scheduler.run_every(interval_minutes=60, job_func=run_bot)
