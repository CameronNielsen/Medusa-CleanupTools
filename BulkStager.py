# This script requires an input called addresses.txt consisting of full paths of the files to be copied into the 
# staging area, one per line. If desired, a supplementary identifier for the staged file can be added after a tab.

filein = open('addresses.txt', 'r')
addresses = filein.readlines()
filein.close()

report = open('DiffReports.txt', 'w')

import subprocess   # This module was a pain to figure out

for raw_addr in addresses:
    raw_addr = raw_addr.replace("\\", "/")    # Cleans the backslashes out of input (because they come from Windows)
        # The following decision tree is to account for different text editors handling of tabs, and the option given
        # to the user to either append a supplemental ID or not.
    if "root" in raw_addr:
        directories_list = raw_addr.split("/")
        root_index = directories_list.index("root")
        coll_id = directories_list[root_index + 1]
        blfg_id = directories_list[root_index + 2]
    else:
        print("Something is wrong with your input!")
        break

    source = str(raw_addr)

    if "\t" in source:
        both_items = source.split("\t")
        source_addr = both_items[0]
        supp_id = both_items[1]
        rsync = ['rsync', '-r', '--progress', "TestZone/root/1114/2565/.", ('./' + coll_id + '-' + supp_id)]
            # The first address won't be hard coded in the final version
        subprocess.call(rsync)
        diff = ['diff', '-r', "TestZone/root/1114/2565/.", ('./' + coll_id + '-' + supp_id)]
        subprocess.call(diff, stdout=report)    # Note to self: THIS is the correct way to pipe stout in subprocess, so
            # DO NOT try to use native Bash operators like >> !

    elif "   " in source:
        both_items = source.split("   ")
        source_addr = both_items[0]
        supp_id = both_items[1]
        rsync = ['rsync', '-r', '--progress', "TestZone/root/1114/2565/.", ('./' + coll_id + '-' + supp_id)]
        subprocess.call(rsync)
        diff = ['diff', '-r', "TestZone/root/1114/2565/.", ('./' + coll_id + '-' + supp_id)]
        subprocess.call(diff, stdout=report)

    else:
        rsync = ['rsync', '-r', '--progress', "TestZone/root/1114/2565/.", ('./' + coll_id)]
        subprocess.call(rsync)
        diff = ['diff', '-r', "TestZone/root/1114/2565/.", ('./' + coll_id)]
        subprocess.call(diff, stdout=report)

report.close()

# Rings the console's bell when copying is complete
subprocess.call(["echo", "-e", "\a"])
subprocess.call(["echo", "-ne", "\007"])
