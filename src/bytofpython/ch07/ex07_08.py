
__author__="jenkinset"
__date__ ="$Jun 10, 2009 12:42:39 PM$"

def printMax(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''

    x = int(x) # convert to integers, if possible
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

printMax(4, 4)
print printMax.__doc__