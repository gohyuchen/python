import sys
import time
from os import system
from random import randint

sys.path.append('/usr/local/lib/python3.9/site-packages')


"""
docstring:
    memory game
    length of number to remember gets longer until you FAIL

    author: gohyuchen
    date: 2023-09-22
    time taken: 1 hour++  
"""

def main():
    player_name = input("Enter your in-game name! \n")
    level = input("What level would you like to start on?\n")
    i = int(level)
    score = 0

    while i <= 30:
        number = randint(max(1,10 ** (i-1))
                            , 10 ** i)
        print(f"Round {i}!, your number = {number}")

        a = 5
        while a > 0:
            print(f"COUNTDOWN TIMER LEFT = {a}")
            time.sleep(1)
            a -= 1
            print ("\033[A                             \033[A")

        print ("\033[A                             \033[A")

        answer = input("Please input your answer now: \n")

        if answer != str(number):
            print(f"game over for {player_name}!")
            print(f"sorry {player_name}! the number was actually {number}")
            print(f"{player_name} got {score} numbers correct!")
            break
        else:
            i += 1
            score += 1


if __name__ == "__main__":
    main()
