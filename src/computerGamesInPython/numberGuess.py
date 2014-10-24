# This is a guess the number game.
import random

guessesTaken = 0

print 'Hello! What is your name?'
name = raw_input()

numberToGuess = random.randint(1, 20)
print 'Well, ' + name + ', I am thinking of a number between 1 and 20.'

while guessesTaken < 6:
	print 'Take a guess:'
	guess = raw_input()
	guess = int(guess)
	guessesTaken += 1
	
	if guess < numberToGuess:
		print 'Your guess is too low.'
	elif guess > numberToGuess:
		print 'Your guess is too high.'
	else:
		break

if guess != numberToGuess:
	numberToGuess = str(numberToGuess)
	print 'Nope. The number I was thinking of was ' + numberToGuess
else:
	guessesTaken = str(guessesTaken)
	print 'Good job, ' + name + '! You guessed my number in ' +	guessesTaken + ' guesses!'