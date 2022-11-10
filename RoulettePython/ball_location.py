import random
import time

def location():
    
    # Chooses a number between 0 and 37
    number =  random.randint(0, 37)

    # Sets the letter to be a blank character
    letter = ""

    # If number is 0 the 'G' will represent the green tile on the board
    if number==0:
        letter = "G"

    # Numbers between 1 and 10 or 19 and 28 have even numbers set to 'B' (Black) and if odd 'R' (Red)
    elif (1<=number<=10) or (19<=number<=28):
        if number%2==0:
            letter = "B"
        else:
            letter = "R"

    # Any other number has evens set to 'R' (Red) and odds to 'B' (Black)
    else:
        if number%2==0:
            letter = "R"
        else:
            letter = "B"

    location = ""
    location_uncolored = letter + str(number)

    # If the letter is 'G', the text will be set to green
    # If the letter is 'R', the text will be set to red
    # Text will remain the same if the letter is 'B'
    if letter == 'G':
        location = "\033[32m" + location_uncolored + "\033[32m \n"
    elif letter == 'R':
        location = "\033[1;31;40m" + location_uncolored + '\n'
    else:
        location = location_uncolored + "\n"

    # Stores the message for where the 'ball' lands
    # 'location_uncolored' is stored to be able to find if the players bet matches the letter, number, or both
    return ("The Ball Landed On " + location), location_uncolored

def main():
    s = location()
    print(s[0])

if __name__ == "__main__":
    main()