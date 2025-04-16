import schedule
import time

def run_every(interval_minutes, job_func):
    schedule.every(interval_minutes).minutes.do(job_func)

    while True:
        schedule.run_pending()
        time.sleep(1)
