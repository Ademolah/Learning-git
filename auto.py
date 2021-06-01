import os
import shutil
import sys

def check_reboot():
    return os.path.exists("/run/reboot-required")

def welcome():
    """ This python script will be used to automate voice activation"""
    print('Everything is Okay')

def check_disk_full(disk, min_gb, min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabyte_free = du.free / 2**30
    if gigabyte_free < min_gb or percent_free < min_percent:
        return True
    return False 

def check_root_full():
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def main():
    checks = [
        (check_reboot, "Pending reboot"),
        (check_disk_full, "Root partition is full")
    ]
    everything_okay = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_okay = False
    
    if not everything_okay:
        sys.exit(1)

    print("Everything is okay ")
    sys.exit(0)

