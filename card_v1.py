import random

"""
docstring:
    Simulates the Lucky Dip experience
"""

CARD_COUNT = 2_000
prize_dict = {
    "Apple Macbook Pro (14-inch, 2021) - Silver": 1,
    "Apple Watch Series 9 GPS, 45mm": 1,
    "Apple Airpods Pro (2nd Generation)": 1,
    "1 Night Stay @ JW Marriott Hotel Singapore South Beach - Deluxe Room": 1,
    "Capitaland Voucher - S$200": 1,
    "Capitaland Voucher - S$150": 1,
    "Capitaland Voucher - S$100": 2,
    "$150 Buffet Dining Voucher at Carousel, Royal Plaza On Scotts Singapore": 2,
    "Sony SRS-XB23 Extra Bass Portable Bluetooth Speaker": 1,
    "Capitaland Voucher - S$80": 2,
    "Capitaland Voucher - S$40": 9,
    "Capitaland Voucher - S$30": 14,
    "Capitaland Voucher - S$20": 5,
    "Shopee Vouchers - S$40 (no min spend)": 7,
    "Shopee Vouchers - S$30 (no min spend)": 19,
    "Shopee Vouchers - S$20 (no min spend)": 31,
}


def main(card_count, prize_dict):
    prize_list = []
    for key in prize_dict:
        while prize_dict[key] > 0:
            prize_list.append(key)
            prize_dict[key] -= 1

    while len(prize_list) > 0:
        input_trigger = input(
            "YEAR-END GET TOGETHER LUCKY D*I*P \nType 'tear' to reveal your prize!\n"
        )

        if input_trigger == "tear":
            win_chance = random.randint(1, card_count)
            if win_chance <= len(prize_list):
                prize = random.choice(prize_list)
                print("You have won a", prize)
                prize_list.remove(prize)
            else:
                print("You have won a BETTER LUCK NEXT TIME")
            card_count -= 1

        else:
            print(
                "The card is still folded! You have to tear the tape and unfold the card to get to the prize!"
            )

    print("everyone else has won a BETTER LUCK NEXT TIME!")


if __name__ == "__main__":
    main(CARD_COUNT, prize_dict)
