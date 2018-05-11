# Generates a tree list of all 0-byte files in a specified directory, arranges them in a tree

import os
import datetime

base_dir = input("Input full path of directory to evaluate: ")
report_name = os.path.basename(base_dir)    # Finds clean base name to identify printed report
outfile = open(report_name + '_0byteReport.txt', 'w')
print(str(datetime.datetime.now()), file=outfile)
print("Base directory: " + base_dir, file=outfile)

for root, dirs, files in os.walk(base_dir):
    level = root.replace(base_dir, '').count(os.sep)  # Counts the separators to determine how many levels down
    # from the base directory we are
    indent = '  ' * level
    print('{}{}/'.format(indent, os.path.basename(root)), file=outfile)
    subindent = '   ' * (level + 1)
    for file in files:
        location = os.path.join(root, file)
        if os.path.getsize(location) == 0:
            print('{}{}'.format(subindent, file), file=outfile)

outfile.close()