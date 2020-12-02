from random import randint
import math


def play():
    random_int = randint(1, 100)
    counter: int = 0
    while True:
        counter = counter + 1
        user_guess = int(input("Enter the number : "))
        if user_guess > random_int:
            print("Too Much.. Reduce..")
            continue
        if user_guess < random_int:
            print("Too Less.. Increase")
            continue
        if user_guess == random_int:
            print("Ding.. Ding.. Ding.. your the winner..\nYou have found with %d tries" % counter)
            break


if __name__ == '__main__':
    play()
