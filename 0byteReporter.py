# Generates a list of all 0-byte files in a specified directory, arranged in a tree.

import os
import datetime

base_dir = input("Input full path of directory to evaluate (using forward slashes): ")
report_name = os.path.basename(base_dir)    # Finds clean base name to identify printed report
outfile = open(report_name + '_0byteReport.txt', 'w')
print(str(datetime.datetime.now()), file=outfile)  # Adds creation date information to report
print("Base directory: " + base_dir, file=outfile)  # Adds scanned location information to report

for root, dirs, files in os.walk(base_dir):
    level = root.replace(base_dir, '').count(os.sep)  # Counts the separators to determine how many levels down
    indent = '  ' * level
    print('{}{}/'.format(indent, os.path.basename(root)), file=outfile)
    subindent = '   ' * (level + 1)
    for file in files:
        location = os.path.join(root, file)
        if os.path.getsize(location) == 0:  # Detects and prints only empty files
            print('{}{}'.format(subindent, file), file=outfile)

outfile.close()
