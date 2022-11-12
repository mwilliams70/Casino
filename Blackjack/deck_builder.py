import card

SUITS=["H", "C", "D", "S"]
NUMBERS=[1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

def deck_builder(deck_list):
    for suit in SUITS:
        for number in NUMBERS:
            c=card.Card(number, suit)
            deck_list.append(c)

