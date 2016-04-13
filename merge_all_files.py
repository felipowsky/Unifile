#!/usr/bin/env python

import os
import sys

extensions = ['.h', '.m', '.swift']
final_filename = 'merged_file.txt'
filepaths = []
directory = os.getcwd()

if len(sys.argv) > 1:
    arg = sys.argv[1]
    directory = arg

if os.path.isdir(directory):
    print('Searching files...')

    for dirpath, dirs, filenames in os.walk(directory):
        for filename in filenames:
            ext = (os.path.splitext(filename)[1]).lower()
            if ext in extensions:
                filepaths.append(os.path.join(dirpath, filename))

    if len(filepaths) < 1:
        print('No files found.')

    else:
        filepaths.sort(key=lambda filepath: (os.path.split(filepath)[1]).lower())

        print('Exporting to ' + os.path.join(os.getcwd(), final_filename))

        with open(final_filename, 'w') as outfile:
            for filepath in filepaths:
                with open(filepath) as infile:
                    for line in infile:
                        outfile.write(line)

                    outfile.write('\n')

        print('Done.')

else:
    print('Invalid directory ' + repr(directory))
