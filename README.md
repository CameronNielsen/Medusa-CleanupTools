# Medusa-CleanupTools

A suite of Python tools for cleaning up legacy digital collections. It's also my final class project for IS 452.


## SafeMassCopy
This is a script for copying files over into local working directories for restructuring. The tricky thing with this one was figuring out how to run Bash commands from within Python, because I wanted it go through rsync. The documentation for subprocess module was quite opaque to me, and I had to put my head together with another random student to puzzle it out. I tried a lot of different syntax arrangments before I was able to work out all the different decisions and variable flows you see in the finished product.
And something like this takes a lot of debugging, rewriting, and retrying, because you have to build it around how your actual filesystem reacts, not to mention your workflow. In this case, for example, I ran into a problem with backslashes being interpreted by Python as special character, even when within a string (well, where else would they), since my address list would be coming from a Windows computer, but then need to be used on a Linux VM where the actual restructuring takes place. I suppose doing that particular bit of text cleaning on addresses is something I'm going to have to make standard on all my scripts going forward.
I tried to introduce some flexibility as far as what kinds of inputs or uses you can use, but as you can see even a little of that added a lot of complexity. Hopefully I'll figure out a more architecturally simple way to make it a little more flexible in the future, right now it's very much for one particular kind of staging operation, taking one particular kind of input.
