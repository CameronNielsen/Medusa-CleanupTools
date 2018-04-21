# def main():  #I might want to use this later, not sure.

import os

topdir = input("Enter the full path of the directory to scan: ") #The starting point for walk
movedir = input("Enter the full path of the directory to move 0-byte files to: ")
logname = 'find0bytes.log'
results = str()

for dirpath, dirnames, filenames in os.walk(topdir):
    for name in filenames:
        location = os.path.join(dirpath, name)
        if os.path.getsize(location) == 0:  #Does the actual detection of the problematic file size
            movepath = os.path.join(movedir, name)
            results += '%s\n' % os.path.join(dirpath, name)
            if os.path.exists(movepath): #I had to add this decision tree to prevent clobbering
                counter = 0
                while os.path.exists(movepath):  #Looks for a new name that isn't already taken
                    counter = counter + 1
                    nameparts = name.split(".")
                    newname = nameparts[0] + "_" + str(counter) + "." + nameparts[1]
                    movepath = os.path.join(movedir, newname)
                os.rename(location, movepath)
            else:
                os.rename(location, movepath)

# Write results to logfile, also checking to not overwrite preexisting logs
if os.path.exists(logname):
    counter = 0
    while os.path.exists(logname):
        counter = counter + 1
        nameparts = logname.split(".")
        logname = nameparts[0] + "_" + str(counter) + "." + nameparts[1]

with open(logname, 'w') as logfile:
    logfile.write(results)

# if __name__ == '__main__':
#     main()


# Commentary: testing was tricky, because it had to be done on a linux machine. Bash command "touch" was used to create 0-byte files to test on within a mock nested file structure. I also made the mistake of running it on my entire working directory...turns out PyCharm includes some 0-byte files in the venv. So I had to reboot my Python interpreter setup...

#Original model, from https://www.pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1

# import os
#
# # The top argument for walk
# topdir = '.'
# # The extension to search for
# exten = '.txt'
# logname = 'findfiletype.log'
# # What will be logged
# results = str()
#
# for dirpath, dirnames, files in os.walk(topdir):
#     for name in files:
#         if name.lower().endswith(exten):
#             # Save to results string instead of printing
#             results += '%s\n' % os.path.join(dirpath, name)
#
# # Write results to logfile
# with open(logname, 'w') as logfile:
#     logfile.write(results)
