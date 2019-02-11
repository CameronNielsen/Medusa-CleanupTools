import os
import glob
import subprocess

cwd = os.getcwd()

for item_level_dir in os.listdir(cwd):
    item_level_path = os.path.join(cwd, item_level_dir)
    search_path = os.path.normpath(item_level_path + os.sep + "**" + os.sep + "VIDEO_TS" + os.sep)
    found_content_dirs = glob.glob(search_path, recursive=True)
    if len(found_content_dirs) == 0:
        print("ERROR:", item_level_path, "does not contain correctly formatted DVD files!")
    else:
        for content_dir in found_content_dirs:
            content_dir = os.path.normpath(content_dir)
            output_file_name = item_level_dir + "_deriv.mp4"
            output_file_path = os.path.join(content_dir, output_file_name)
            subprocess.run(["C:\Program Files\HandBrake\HandBrakeCLI.exe", "-i", content_dir, "-o", output_file_path, "-e", "x264", "-q", "20", "-B", "160"])
            print(output_file_path, "has been created.")
