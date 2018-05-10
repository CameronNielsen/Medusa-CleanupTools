import os

working_dir = input("Input full path of directory to evaluate: ")

for root, dirs, files in os.walk(working_dir):
        level = root.replace(working_dir, '').count(os.sep)
        indent = '|  ' * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = '|  ' * (level + 1)
        for file in files:
                location = os.path.join(root, file)
                if os.path.getsize(location) == 0:
                        print('{}{}'.format(subindent, f))
                # I'd like to replace this part with a loop that, instead of 
                # listing each individual file, lists the first few of each file
                # extension, then provides a count of how many of that type there are
                # in the directory. This should be simple enough.

# duration = 1  # second
# freq = 440  # Hz
# os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
