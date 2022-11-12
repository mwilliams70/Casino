import card

SUITS=["H", "C", "D", "S"]
NUMBERS=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

def deck_builder(deck_list):
    #Goes through each suit, {Hearts, Clubs, Diamonds, Spades}
    for suit in SUITS:
        #Goes through each number {2-10, then Jack, Queen, King, Ace}
        for number in NUMBERS:
            #makes a Card with each suit and number
            c=card.Card(number, suit)

            #card is added to the deck
            deck_list.append(c)
