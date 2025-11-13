import psutil
import time
import logging

logging.basicConfig(filename="system_health.log", level=logging.INFO)

CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 90

while True:
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    if cpu > CPU_THRESHOLD or mem > MEM_THRESHOLD or disk > DISK_THRESHOLD:
        logging.warning(f"High usage detected: CPU={cpu}%, MEM={mem}%, DISK={disk}%")
    else:
        logging.info(f"Normal: CPU={cpu}%, MEM={mem}%, DISK={disk}%")

    time.sleep(10)
