
__author__="jenkinset"
__date__ ="$Jun 10, 2009 8:13:31 AM$"

number = 23
guess = int(raw_input('Enter an integer : '))

if guess == number:
    print 'Congratulations, you guessed it.' # New block starts here
    print "(but you do not win any prizes!)" # New block ends here

elif guess < number:
    print 'No, it is a little higher than that' # Another block

else:
    print 'No, it is a little lower than that'
    # You must have guess > number to reach here

print 'Done'
# This last statement is always executed, after the if statement is executed

