from random import randint
import sys


def run_guess(str_guess, answer):
    # Check guess against answer and respond
    try:
        guess = int(str_guess)
    except ValueError:
        return False, 'please enter a number: '

    if 0 < guess < 11:
        if guess == answer:
            return True, 'you are a genius!'
        else:
            return False, 'guess again: '
    else:
        return False, 'hey bozo, I said 1~10: '


if __name__ == '__main__':
    # generate a random number 1~10
    answer = randint(1, 10)
    message = 'guess a number 1~10:  '
    guess_is_correct = False
    # Loop until user guesses correctly
    while not guess_is_correct:
        guess_is_correct, message = run_guess(input(message), answer)
    print(message)



