import subprocess
import csv
import time
from datetime import datetime

file = open("cpu_usage.csv", "a", newline="")
writer = csv.writer(file)

writer.writerow(["timestamp", "pod", "cpu"])

print("Collecting CPU metrics...")

while True:
    result = subprocess.run(
        ["kubectl", "top", "pods"],
        capture_output=True,
        text=True
    )

    lines = result.stdout.split("\n")[1:]

    for line in lines:
        if line:
            parts = line.split()
            pod = parts[0]
            cpu = parts[1].replace("m", "")

            writer.writerow([
                datetime.now(),
                pod,
                cpu
            ])

    file.flush()
    time.sleep(10)
