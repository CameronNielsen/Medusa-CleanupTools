# Medusa-CleanupTools

A suite of Python tools for cleaning up legacy digital collections. It's also my final class project for IS 452. These are simple scripts for performing well-defined tasks as part of my regular duties, so they are designed to be run in a Linux console (by cd'ing to their working location and then invoking them with "python3 scriptName.py"), sometimes with inputs from my Windows workstation (ie, they're designed to tolerate input addresses with backslashes). As of my final submission for that class, the project includes the following 5 finished scripts:

## 0byteRemover.py
Recursively detects empty files (with filesize of 0 bytes) from a location specified via user input, then moves them to another specified directory for inspection and/or deletion. Automatically renames identically-named files to prevent clobbering. Prints list of removed file paths to txt file in default working location.



