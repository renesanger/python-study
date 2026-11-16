# This is a guess the number game.
import random 

secret_number = random.randint(1,20)
print('I am thinking of a number between 1 and 20')

# Ask the player to guess 6 times
for guesses_taken in range(1,7):
    print('Take a guess')
    guess = int(input('>'))

    if guess < secret_number:
        print('Your guess is too low')
    elif guess > secret_number:
        print('Your guess is too high')
    else:
        break # This condition is the correct guess

if guess == secret_number:
    print('Good Job! You got it in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number was ' + str(secret_number))

"""
print('I am thinking of a number between 1 and 20')
print('Take a guess')
answer = 16
numGuesses = 0
while True:
    guess = int(input('>'))
    numGuesses += 1

    if guess < answer:
        print('Your guess is too low')
    elif guess > answer:
        print('Your guess it too high')
    else:
        print('Good Job! You got it in ' + str(numGuesses) + ' guesses.')
        break

The difference betweeen your solution and the given solution are
we use the random.randint() function
we limit the number of guesses to 7 and we print the iteration of thee loop where it ended.
brother your solution was close but cmon man... do better.

"""