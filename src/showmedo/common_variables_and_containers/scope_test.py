a = 1
print "before for loop:", a, id(a)

# simple for loop, looks like a nested block in some languages
for n in range(3):
    a = 2
print "after for loop:", a, id(a)

def my_fn():
    global a # in practice, generally AVOID globals
    print "in my_fn, before assignment", a, id(a)
    a = 4  # This local 'a' masks the other 'a' -- it's a different object
    print "in my_fn:", a, id(a)
    
my_fn() # call my_fn to test scoping rules
print "after fn call:", a, id(a)
