import os

working_dir = input("Input full path of directory to evaluate: ")

for root, dirs, files in os.walk(working_dir):
        level = root.replace(working_dir, '').count(os.sep)
        indent = '|  ' * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = '|  ' * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

duration = 1  # second
freq = 440  # Hz
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
