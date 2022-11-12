import deck_builder as db
import random

def main():
    deck=[]
    db.deck_builder(deck)
    # random.shuffle(deck)
    print(deck)
    c1=deck.pop(len(deck)-1)
    c2=deck.pop(12)
    print("Your cards are: " + str(c1) + " and " + str(c2) + "\n")

    # Gets the value of the two cards 
    number1=c1.get_number()
    number2=c2.get_number()

    """
    Checks for the Cards value, If it is {J, Q, or K} the value will be set to 10
    If the value is 'A', the value is set to 11
    """
    if c1.get_number() == "J" or c1.get_number() == "Q" or c1.get_number() == "K":
        number1=10
    if c2.get_number() == "J" or c2.get_number() == "Q" or c2.get_number() == "K":
        number2=10
    if c1.get_number() == "A":
        number1=11
    if c2.get_number() == "A":
        number2=11

    total = int(number1)+int(number2)
    print("Your total is: " + str(total))

    print(deck)
    

main()