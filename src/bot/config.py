import os
from dotenv import load_dotenv

load_dotenv()

# آدرس کامل ADB برای MEmu
ADB_PORT = os.getenv("MEMU_ADB_PORT", "21503")
ADB_ADDRESS = f"127.0.0.1:{ADB_PORT}"

# مسیر فایل‌ها
SCREENSHOT_PATH = os.getenv("SCREENSHOT_PATH", "screen.png")
COLLECTOR_IMAGE_PATH = os.getenv("COLLECTOR_IMAGE_PATH", "assets/collector_full.png")
