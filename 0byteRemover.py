# Recursively detects empty files (with filesize of 0 bytes) from a specified location, then moves them to another specified 
# directory for inspection and/or deletion. Automatically renames identically-named files to prevent clobbering. Prints
# listing of removed file paths to txt file in default working location.

import os
import datetime

topdir = input("Enter the full path of the directory to scan: ") #The starting point for walk. If working in the default
    # directory, DO NOT put a slash in front! That mistake made me do so much misguided debugging...
movedir = input("Enter the full path of the directory to move 0-byte files to: ")
logname = '0bytesRemovedReport.txt'
results = str()

for root, dirs, files in os.walk(topdir):
    for name in files:
        location = os.path.join(root, name)
        if os.path.getsize(location) == 0:  #Does the actual detection of the problematic file size
            movepath = os.path.join(movedir, name)
            results += '%s\n' % os.path.join(root, name)
            if os.path.exists(movepath):  #I had to add this decision tree to prevent clobbering
                base_filename = str(os.path.splitext(name)[0])
                file_ext = str(os.path.splitext(name)[1])
                counter = 0
                while os.path.exists(movepath):  #Looks for a new name that isn't already taken
                    counter += 1
                    newname = base_filename + "_" + str(counter) + file_ext
                    movepath = os.path.join(movedir, newname)
                os.rename(location, movepath)
            else:
                try:              # Deals with the error caused if you did not create a destination directory first
                    os.rename(location, movepath)
                except FileNotFoundError:
                    print("\nERROR: You need to create the destination directory first!")

# Write results to logfile, also checking to not overwrite preexisting logs
if os.path.exists(logname):
    base_logname = str(os.path.basename(logname)).split('.')[0]
    counter = 0
    while os.path.exists(logname):
        counter += 1
        logname = base_logname + "_" + str(counter) + ".txt"

report = open(logname, 'w')
print("The following files removed at", str(datetime.datetime.now()), '\n', file=report)  #Writes a date/time heading
report.write(results)  # Writes the removed files list
report.close()

# Commentary: testing was tricky, because it had to be done on a linux machine. Bash command "touch" was
# used to create 0-byte files to test on within a mock nested file structure. I also made the mistake of
# running it on my entire working directory...turns out PyCharm includes some 0-byte files in the venv.
# So I had to create my Python interpreter setup.
# Debugging was torturous, and I ended up completely rewriting the filename clobbering avoidance sections 
# to use os.path because my original version, using just string manipulation, spat out weird stuff in 
# certain circumstances.
