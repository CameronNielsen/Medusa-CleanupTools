# This script requires an input called addresses.txt consisting of full paths of the files to be copied, one per line.
# If desired, a supplementary identifier or name for the staged file can be added after a tab.

filein = open('addresses.txt', 'r')
test_strings = filein.readlines()
filein.close()

# This function finds the collection ID number from the Medusa file system, which is always immediately under the root directory.
def find_coll_id(source_addr):
    if "root" in source_addr:
        directories_list = source_addr.split("/")
        root_index = directories_list.index("root")
        collection_id = directories_list[root_index + 1]
        return collection_id
    else:
        print("You're using the wrong script!")

# def run_rsync(args):
#     import subprocess
#

for raw_input in test_strings:
    raw_input = raw_input.replace("\\", "/")
    if "\t" in raw_input:
        both_items = raw_input.split("\t")
        raw_source = both_items[0]
        supp_id = both_items[1]
        coll_id = find_coll_id(raw_source)
        print(coll_id, supp_id)


    elif "    " in raw_input:
        both_items = raw_input.split("    ")
        raw_source = both_items[0]
        supp_id = both_items[1]
        coll_id = find_coll_id(raw_source)
        print(coll_id, supp_id)

    else:
        coll_id = find_coll_id(raw_input)
        print(coll_id)

