# Medusa-CleanupTools

A suite of Python tools for cleaning up legacy digital collections. It's also my final class project for IS 452.

**For the midpoint check in**:

What I have so far is one fairly polished module, the 0-byte crawler. Since beginning the project, I have elaborated upon my initial prototype to give it the ability to avoid clobbering. I've also just generally tested it more carefully and made it more robust.

As for the other modules, what I have so far is a start on a report generator, to create tree diagrams and sound a bell when processes are finished. This bit still consists of pasted-together recipes that I haven't fully reverse-engineered yet (they do work, though). Once I have a better idea of how they work, I'll want to intigrate these functions back into my main modules.

Otherwise, I have been studying how to use Bash from within Python to handle some of the other file operations, since for the purposes of my job we would prefer to handle file copying using rsync and such. As far as creating a progress bar for this process once automated, someone has already written a python script to do it: https://gist.github.com/JohannesBuchner/4d61eb5a42aeaad6ce90. The trouble is, it doesn't seem to be working. So one of the next things I will want to do is figure that out and create a version of my own that works better on my system.

I also looked into using Curses to print color-coded text, and decided anything involving Curses was Not Worth It. I don't need colored output text, and there seem to be other ways of making notification sounds to try if the method I included already doesn't work on my work console.

The main thing I'm still not sure about is how to make these different functions relate to one another as part of a workflow. Do I want them to be modules of a master program, or just scripts to run incrementally? Or do I want to package them so they can run as console commands on their own (I suppose by putting them in my system path)? How developed do these connections between modules need to be, for the purposes of this assignment?
