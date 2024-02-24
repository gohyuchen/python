import pprint
import random
import time

"""
docstring:
    Simulates the Lucky Dip experience
    Toggle True/False in 'main' to use fake list
"""

prize_dict = {
    "Apple Watch": 1,
    "Prize#2": 2,
    "Nice cake": 3,
    "Box of chocolates": 4,
    "$20 voucher": 5,
    "$10 voucher": 6,
    "$5 voucher": 7,
    "$2 voucher": 8,
    # "P9": 9,
    # "P10": 10,
}


def main(prize_dict, generate_participant_list):
    participant_list = []

    if generate_participant_list == False:
        participant_list = list(range(1, 100+1))
    else:
        while True:
            new_participant = input("Do you want to add another participant? y/n\n")
            if new_participant == "y":
                participant_name = input("Please input the participant's name:\n")
                if participant_name in participant_list:
                    print(f"This name '{participant_name}' has already been taken, please input a unique name!")
                    continue
                else:
                    pass

                participant_list.append(participant_name)
                print(f"Current list of participants is {participant_list}")
                continue
            else:
                print("We are not adding any more participants!")
                break

    total_participant = len(participant_list)
    print(f"There are {total_participant} participants in our lucky draw!")
    # print(f"The participants are {participant_list}")
    
    prize_list = []
    for key in prize_dict:
        while prize_dict[key] > 0:
            prize_list.append(key)
            prize_dict[key] -= 1
    # print(f"The prize list stands at: {prize_list}")
    input("Press Enter to begin our lucky draw!")
    final_winners = {}
    while total_participant > 0:
        win_chance = random.randint(1, total_participant)
        winning_participant = participant_list.pop(0)
        if win_chance <= len(prize_list):
            prize = random.choice(prize_list)
            print(f"{winning_participant} has won a {prize}")
            final_winners[winning_participant]=prize
            prize_list.remove(prize)
        else:
            print(f"{winning_participant} has won a BETTER LUCK NEXT TIME")
        
        total_participant -= 1
        print(f"Current participants left to draw is {total_participant}")
        print(f"There are {len(prize_list)} prizes remaining")
        # print(f"Remaining prize list stands at: {prize_list}")
        # time.sleep(1)
        if total_participant > 0:
            print(f"----------NEXT DRAW----------")
        else:
            print(f"----------END OF DRAW----------")
            print(f"These are the non-'BETTER LUCK NEXT TIME' winners: \n ")
            for winner in final_winners:
                print(f"{winner}:{final_winners[winner]}")


if __name__ == "__main__":
    main(prize_dict, generate_participant_list=False)
