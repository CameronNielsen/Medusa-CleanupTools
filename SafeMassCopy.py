# This script requires an input called addresses.txt consisting of full paths of the files to be copied, one per line.
# If desired, a supplementary identifier or name for the staged file can be added after a tab.

filein = open('addresses.txt', 'r')
test_strings = filein.readlines()
filein.close()

for raw_input in test_strings:
    if "    " in raw_input:
        both_items = raw_input.split("  ")
        raw_source = both_items[0]
        supp_id = both_items[1]
        print(raw_source, supp_id)
    else:
        raw_source = raw_input
        print(raw_source)

    if "root" in raw_source:
        directories_list = raw_source.split("\\")
        root_index = directories_list.index("root")
        collection_ID = directories_list[root_index + 1]
        print(collection_ID)
    else:
        print("You're using the wrong script!")






# subprocess.run()