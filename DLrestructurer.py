filein = open("KoopmanFileList.txt", mode='r')
import glob
import shutil
import os

filelist = filein.readlines()
for object in filelist:
    object = object.strip("\n")
    dir1 = os.path.join("E:/Koopman/" + object)
    os.mkdir(dir1, mode=0o777)
    dir2 = os.path.join("E:/Koopman/" + object + "/access")
    os.mkdir(dir2, mode=0o777)
    dir3 = os.path.join("E:/Koopman/" + object + "/preservation")
    os.mkdir(dir3, mode=0o777)
    jp2_origin = os.path.join("E:/Preservation/access/" + object + ".jp2")
    jp2_dest = os.path.join("E:/Koopman/" + object + "/access/" + object + ".jp2")
    shutil.copy2(jp2_origin, jp2_dest)
    tif_origin = os.path.join("E:/Preservation/access/" + object + ".tif")
    tif_dest = os.path.join("E:/Koopman/" + object + "/preservation/" + object + ".tif")
    shutil.copy2(tif_origin, tif_dest)
filein.close()



# for file in filelist:
#     file = os.path.normpath(file)
#     file_name = os.path.basename(file)
#     id_number = file_name.split("_")[0]
#     dest_dir_loc = os.path.join(dest, id_number)
#     if os.path.exists(dest_dir_loc):
#         subdir = glob.glob(dest_dir_loc + '/0**/')
#         for sub_path in subdir:
#             sub_path = os.path.normpath(sub_path)
#             origin_path = os.path.join(origin + file_name)
#             dest_path = os.path.join(sub_path + "/PDI/ObjectJPG/" + file_name)
#             shutil.copy2(origin_path, dest_path)
#     else:
#         print(dest_dir_loc, "does not exist!")