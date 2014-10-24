#!/usr/bin/env python

def check_fermat(a, b, c, n):
    if((a**n)+(b**n)==(c**n) and n > 2):
        print "Holy smokes, Fermat was wrong!"
    else:
        print (a**n)
        print (b**n)
        print (c**n)
        print "No, that doesn't work."

a = input("Enter a value for a: ")
b = input("Enter a value for b: ")
c = input("Enter a value for c: ")
n = input("Enter a value for n: ")

check_fermat(a, b, c, n)