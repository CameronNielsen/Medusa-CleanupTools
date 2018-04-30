import glob
import shutil
import os

# fileext = input("Enter file extension of the files you want to move (without the dot): ")
# origin = input("Enter full path of the directory files to be moved are located in (ending with /): ")
# dest = input("Enter full path of the directory files are to be sorted into (ending with /): ")
fileext = "txt"
origin = "./Test/"
dest = "./Test/"

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
# To do: Add comments, make input/output less brittle, clean out ALL back slashes, add error messages for files not
# present, fix whatever makes it crash with large numbers of big files
# New To Do after talking to Henry: use os.path for all cleanup of addresses, etc. Error handling for if no files.
# Use debugger to figure out what's going wrong!
# Update 4/30 --I think it's done?! Except for comments and some stress testing?
