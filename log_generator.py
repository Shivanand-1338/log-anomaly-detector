import random
from datetime import datetime
import time

normal_logs = [
    "INFO User login successful",
    "INFO File uploaded",
    "INFO Payment processed",
    "INFO User logout",
    "INFO Health check passed"
]

anomalous_logs = [
    "ERROR User login failed",
    "CRITICAL Disk space full",
    "ALERT Multiple failed login attempts",
    "FATAL Unauthorized access attempt detected"
]

def generate_logs():
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if random.random() < 0.05:  # 5% anomaly chance
            log = f"{now} {random.choice(anomalous_logs)}"
        else:
            log = f"{now} {random.choice(normal_logs)}"
        with open("logs.txt", "a") as f:
            f.write(log + "\n")
        time.sleep(0.5)  # half second delay

if __name__ == "__main__":
    generate_logs()
