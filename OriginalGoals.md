1.	An error-detecting filesystem crawler that can recursively walk a large directory tree and flag trouble items, such as empty (0-byte) files.
2.	Automatic secure copy and staging of collections to be restructured (using rsync, diff, and possibly md5sum comparison), with time-to-completion estimation. (This bit would most likely be in Bash, rather than Python, primarily.)
3.	Audio alerting for when user input is needed or processes complete (maybe using curses.beep?).
4.	Visually-rich reporting, with detected files printed in a tree structure (like the classic “tree” command), progress bars, color coding, etc.
5.	A more advanced crawler that can check to see if filesystems conform to one of a set of packaging profiles specified by the user, while providing clean location data for easy repair.
6.	Scripts to restructure specific types of legacy filesystem to fit the newer packaging profile.
7.	Advanced duplicate detection and removal using md5sums.
8.	Storage of metadata, changes, etc. in a SQLite database (or at least a dictionary).
9.	A basic text terminal GUI implemented in Curses.
