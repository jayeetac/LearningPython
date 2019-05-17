#Generate 1 random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
x = random.randint(1,9)
guess = int(input('Guess the number I chose between 1 and 9'))
while x!= guess:
    if x< guess:
        print('You guessed too high')
    else:
        print('You guessed too low')
    guess = int(input('Guess the number I chose between 1 and 9'))

print ('correct!')
