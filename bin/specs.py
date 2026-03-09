import psutil
import platform
import os
import subprocess

def run(options):
    print("Getting System Specs...\n")

    cpu = platform.processor()
    if not cpu:
        cpu = "Unknown CPU"
    print("CPU: ", cpu)

    ram = round(psutil.virtual_memory().total / (1024.0 ** 3), 2)
    print("RAM: ", ram, "GB")

    disk = psutil.disk_usage(os.path.expanduser("~"))
    total_disk = round(disk.total / (1024.0 ** 3), 2)
    print("Disk Space: ", total_disk, "GB")

    try:
        result = subprocess.run(["wmic", "path", "win32_VideoController", "get", "name"], capture_output=True, text=True, check=True)
        gpu_list = [line.strip() for line in result.stdout.splitlines() if line.strip() and "Name" not in line]
        gpu = ", ".join(gpu_list) if gpu_list else "Unknown GPU"
    except Exception:
        gpu = "Unknown GPU"

    print("GPU: ", gpu)