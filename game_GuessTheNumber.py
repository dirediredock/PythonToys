# GUESS THE NUMBER

# Run this on Terminal. This game will create a three digit number,
# and through hints the goal is to guess the three digit number within
# a number of attempts.

import random

NUM_DIGITS = 4
NUM_GUESSES = 15

print('\nGUESS THE NUMBER')


def main():
    print('\nThere is a {}-digit number in my mind. '.format(NUM_DIGITS) +
          'These digits are numbers from 0 to 9, ' +
          'each potentially found in any of ' +
          'the {} slots.'.format(NUM_DIGITS))
    print('\nA Win! means a digit is correct but in a wrong slot.')
    print('A WinWin! means digit is correct and in the correct slot.')
    print('\nYou have {} attempts. Go!\n'.format(NUM_GUESSES))

    while True:

        # Here the secret number be stored, its a string!

        secretNum = getScecretNum()

        # Initialize the 'numGuesses' counting system.

        numGuesses = 1

        while numGuesses <= NUM_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > NUM_GUESSES:
                print('You ran out of guesses...')
                print('The number was {}'.format(secretNum))

        print('Do you want to play again? [yes or no]')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing! Goodbye.')


def getScecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''

    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

        # This will loop, starting at 1 and ending at 'NUM_DIGITS', exporting
        # the first shuffled digit, then the first and second, then the first
        # and second and third, and so on. It stops at 'NUM_DIGITS' length,
        # and that is what is returned as 'secretNum'

    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('WinWin!!')
        elif guess[i] in secretNum:
            clues.append('Win!')

    if len(clues) == 0:
        return 'No Match'

    # Sort-scramble the clues to not give them away.

    else:
        clues.sort()
        return ' '.join(clues)


# '__main__' is the name of the scope in which top-level code executes.
# A module’s __name__ is set equal to '__main__' when read from standard
# input, a script, or from an interactive prompt.

# More info: https://stackoverflow.com/questions/419163/
# what-does-if-name-main-do

if __name__ == '__main__':
    main()
