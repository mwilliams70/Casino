"""
Provides a constructor for a playing card
"""
class Card:
    __slots__ = ['__number', '__suit']
    def __init__(self, number, suit):
        self.__number=number
        self.__suit=suit

    def get_number(self):
        return self.__number

    def get_suit(self):
        return self.__suit

    
    # Prints the card in the format <Number><First Letter of Suit>
    def __str__(self):
        a_string= str(self.__number) + self.__suit
        return a_string
