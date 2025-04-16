from bot import adb_tools, analyzer, controller, scheduler

def run_bot():
    print("[*] گرفتن اسکرین‌شات...")
    adb_tools.take_screenshot()

    print("[*] جستجو برای کالکتور پر...")
    points = analyzer.find_template_on_screen("screen.png", "assets/collector_full.png")

    if points:
        print(f"[+] یافت شد در مختصات: {points[0]}")
        controller.tap_on_point(*points[0])
    else:
        print("[-] چیزی پیدا نشد.")

if __name__ == "__main__":
    print("[*] اجرای ربات آغاز شد...")
    scheduler.run_every(interval_minutes=60, job_func=run_bot)  # هر 60 دقیقه اجرا شود
