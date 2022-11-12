import card

SUITS=["H", "C", "D", "S"]
NUMBERS=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

def deck_builder(deck_list):
    for suit in SUITS:
        for number in NUMBERS:
            c=card.Card(number, suit)
            deck_list.append(c)

def main():
    deck=[]
    deck_builder(deck)
    i=0
    while i < len(deck):
        print(str(i) + ": " + str(deck[i]))
        i+=1

main()