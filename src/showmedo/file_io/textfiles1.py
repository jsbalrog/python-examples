#!/usr/bin/env python

# open a file for reading in the current directory (needs full path)
f = open('/home/jenkinset/projects/python/showmedo/file_io/textdata_in.txt', 'r')

# read all the lines into a list
lines = f.readlines()

# lines is now a list of strings, so we can iterate over them
for line in lines:
    line = line.strip()
    print line