# Recursively generates a tree diagram of the specified location, listing the total number and size of each file
# extension in each subdirectory.

import os
import math

working_dir = input("Input full path of directory to evaluate: ")
outfile = open('extensionsReport.txt', 'w')


def convert_size(size_bytes):  # Copypasta from StackExchange to make output more human-readable
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

def get_format(location):
    file_utility = ['file', location]
    subprocess.call(file_utility, stdout=report)
    report = str(report)
    return report

def freq(pair):
    return pair[1]


for root, dirs, files in os.walk(working_dir):
    level = root.replace(working_dir, '').count(os.sep)     # There's a bug in my current Linux version of PyCharm
    # that makes .sep not work properly (https://youtrack.jetbrains.com/issue/PY-29249), so forgive me if this spacing
    # bit isn't working right. It worked fine for me before the last PyCharm update. XP
    indent = '|  ' * (level)
    print('{}{}/'.format(indent, os.path.basename(root)), file=outfile)

    subindent = '|  ' * (level + 1)
    ffs_dict = {}
    fsizes_dict = {}

    for file in files:
        location = os.path.join(root, file)
        file_format = get_format(location)
 #       ext = str(os.path.splitext(file)[1])
 #       fsize = os.path.getsize(location)
        if file_format not in ffs_dict:
            counts_dict[file_format] = 1
        else:
            counts_dict[file_format] += 1
        if ext not in fsizes_dict:
            fsizes_dict[fil...........] = fsize
        else:
            fsizes_dict[ext] += fsize

    contents = list(counts_dict.items())
    contents.sort(key=freq, reverse=True)

    for i in contents:
        count = str(i[1])
        ext_key = i[0]
        fsize_total = convert_size(fsizes_dict[ext_key])
        print('{}{}'.format(subindent, i[0] + "\t\t(" + count + ")" + "\t\t" + fsize_total), file=outfile)
        # I want to study .format more so I can make this output look nicer. But it's fine for now.


# Next steps: add option to output to csv
