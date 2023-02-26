#!/usr/bin/env python3
import os
import time
base_path = '/media/usb/touchfiles/icevest'

def remove_files(dir_path, n):
    x = 0
    all_files = os.listdir(dir_path)
    now = time.time()
    n_days = n * 86400
    for f in all_files:
        file_path = os.path.join(dir_path, f)
        if not os.path.isfile(file_path):
            continue
        if os.stat(file_path).st_mtime < now - n_days:
            os.remove(file_path)
            x += 1
            print("Deleted ", f)
    print(str(x) + " files nuked.")

remove_files(base_path, 31 )
