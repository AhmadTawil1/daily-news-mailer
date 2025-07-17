import schedule
import time
import subprocess
import sys

def run_daily_job():
    print("Running daily news job...")
    subprocess.run([sys.executable, "main.py"])

# Schedule the job every day at 07:30 AM
schedule.every().day.at("07:30").do(run_daily_job)

print("✅ Scheduler started — waiting for 07:30...")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)
