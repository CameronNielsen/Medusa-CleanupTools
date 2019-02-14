# Script to find DVD content extracted using our standard born-digital workflow, and then create derivative .MP4
# files using HandBrakeCLI. The latter program is expected to be located at C:\Program Files\HandBrake\HandBrakeCLI.exe.
# The derivative files thus created are placed in a directory called MigratedFiles parallel to the OriginalFiles
# directory already existing.
# The VIDEO_TS directory name is a part of the DVD specification, so it is hard-coded in as both the search term and the
# file name for derivative outputs.

# By Cameron Nielsen, Feb. 12, 2019

import os
import glob
import subprocess

working_dir = input("Enter the full path of the content directory of the collection with DVD videos to convert: ")
# working_dir = os.getcwd()

for item_level_dir in os.listdir(working_dir):
    item_level_path = os.path.join(working_dir, item_level_dir)
    search_path = os.path.normpath(item_level_path + "/**/VIDEO_TS/")
    found_content_dirs = glob.glob(search_path, recursive=True)
    if len(found_content_dirs) == 0:
        log = open("HandBrakeConversion.log", 'w')
        print("NOTE:", item_level_path, "does not contain correctly formatted DVD files!", '\n', file=log)
        log.close()
    else:
        for content_dir in found_content_dirs:
            log = open("HandBrakeConversion.log", 'w')
            content_dir = os.path.normpath(content_dir)
            content_dir_str = str(content_dir)
            disk_level_dir = content_dir_str.split("OriginalFiles")[0]
            migratedfiles_dir = os.path.join(disk_level_dir, "MigratedFiles/")
            output_file_name = os.path.join(migratedfiles_dir + "/VIDEO_TS~d3r1v.mp4")
            migratedfiles_dir = os.path.normpath(migratedfiles_dir)
            output_file_name = os.path.normpath(output_file_name)
            os.mkdir(migratedfiles_dir)
            subprocess.run(["C:\Program Files\HandBrake\HandBrakeCLI.exe", "-i", content_dir, "-o", output_file_name, "-e", "x264", "-q", "20", "-B", "160"])
            print("Converted video file created at", output_file_name, '\n', file=log)
            log.close()
