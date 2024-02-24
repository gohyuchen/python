import time
import urllib.request as urllib2
from random import randint

"""
docstring:
    memory game
    identify whether the word has appeared before!

    author: gohyuchen
    date: 2023-09-27
"""

#set up
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = urllib2.urlopen(word_site)
txt = str(response.read(),'utf-8')
WORDS = txt.splitlines()


def main():
    player_name = input("enter your in-game name \n")
    print("\n")
    seen_list = []
    library_length = len(WORDS)
    round = 0
    
    while round < 1000:
        NEW_OR_OLD = randint(1,10)
        if NEW_OR_OLD <= 2 and round >= 2:
            this_word = seen_list[randint(0,len(seen_list)-1)]
        else:
            index = randint(0,library_length)
            this_word = WORDS[index]

        print(f"word for round {round+1} = {this_word}")
        time.sleep(2)
        print ("\033[A                             \033[A")
        
        answer = input("have you seen this word before? Type y or n only: ")
        if (this_word not in seen_list and answer == 'y') or (this_word in seen_list and answer != 'y'):
            print(f"game over for {player_name}! Your answer is WRONG!")
            print(f"The current list of words is \n")
            print(f"{seen_list}")
            print(f"{player_name} made it to round {round}!!!")
            break

        round += 1
        library_length -= 1
        seen_list.append(this_word)        
        if this_word in WORDS:
            WORDS.remove(str(this_word))
        else:
            continue

if __name__ == "__main__":
    main()
