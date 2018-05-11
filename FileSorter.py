# Sorts PDI photographs by serial number into their appropriate locations in the born-digital reformatting
# output filesystem. Should work on Windows and Linux, but only tested on Windows so far.

import glob
import shutil
import os

fileext = input("Enter file extension of the files you want to move (without the dot): ")
origin = input("Enter full path of the directory files to be moved are located in (ending with /): ")
input("Enter full path of the directory files are to be sorted into (ending with /): ")

files = glob.glob(origin + '*.' + fileext)

for file in files:
    file = os.path.normpath(file) 
    file_name = os.path.basename(file)
    id_number = file_name.split("_")[0]
    dest_dir_loc = os.path.join(dest, id_number)
    if os.path.exists(dest_dir_loc):
        subdir = glob.glob(dest_dir_loc + '/0**/')
        for sub_path in subdir:
            sub_path = os.path.normpath(sub_path)
            origin_path = os.path.join(origin + file_name)
            dest_path = os.path.join(sub_path + "/PDI/ObjectJPG/" + file_name)
            shutil.copy2(origin_path, dest_path)
    else:
        print(dest_dir_loc, "does not exist!")

        # Future goals: make it more flexible so it can be used to sort files in other contexts as well.
