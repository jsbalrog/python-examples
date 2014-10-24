# open a file for reading in the current directory (needs full path)
f = open('/home/jenkinset/projects/python/showmedo/file_io/textdata_in.txt', 'r')

# read all the lines into a list
lines = f.readlines()

ages = [] # an empty list for pairs of names and ages

for line in lines:
    name = line.strip()
    # note int() conversion of string->int
    # also note that there's no error handling here for bad input
    age = int(raw_input("What is %s's age? " % (name)))
    ages.append((name, age)) # (name, age) is a tuple
    
# print the name, age pairs
print ages

# open a second file for writing (will replace any existing)
fo = open('/home/jenkinset/projects/python/showmedo/file_io/textdata_out.txt', 'w')
# iterate over each line of ages, print name then age then carriage-return
for name, age in ages:
    fo.write('%s, %d\n' % (name, age))
    
# tidy up by closing the file to flush all writes, not strictly necessary
# as files are closed when the script finishes anyway
fo.close()