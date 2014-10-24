def compare(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0
    
a = input("First number: ")
b = input("Second number: ")

if compare(a, b) == 1:
    print "First number is greater than second number"
elif compare(a,b) == -1:
    print "Second number is greater than first number"
else:
    print "First and second numbers are the same"    