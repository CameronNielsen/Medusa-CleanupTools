import glob
import shutil

fileext = input("Enter file extension of the files you want to move (without the dot): ")
origin = input("Enter full path of the directory files to be moved are located in (ending with /): ")
dest = input("Enter full path of the directory files are to be sorted into (ending with /): ")


files = glob.glob(origin + '*.' + fileext)

for file in files:
    file_name = file.split("/")[-1]
    file_name = file_name.split("\\")[-1]
    print(file_name, "1")
    file_title = file_name.split(".")[0]
    print(file_title, "2")
    id_number = file_title.split("_")[0]
    print(id_number, "3")
    direct = glob.glob((dest + '%s/') % id_number)[0]
    print(direct)
    subdir = glob.glob(direct + '0**/')
    print(subdir)
    for sub_path in subdir:
        sub_path = sub_path.replace("\\", "/")
        shutil.copy2((origin + file_name), (sub_path + "PDI/ObjectJPG/" + file_name))

#To do: Add comments, make input/output less brittle, clean out ALL back slashes, add error messages for files not present, fix whatever makes it crash with large numbers of big files