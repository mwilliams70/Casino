import re
import ball_location

def command_prompts(location):
    print("Enter 'help' for commands")
    while True:
        user_input = input(">> ")

        # Sets user_input conditions to exit the loop
        if user_input == "" or user_input=="quit":
            break

        # If the user enters 'help' a list of commands with examples will print
        elif user_input=="help":
            print(
            "bet - (R, B, G)(0-37) + *SPACE* + Bet Amount\n" + 
            "      if multiple bets, seperate by comma: R 38 3000, B 23 2500... \n"
            "help - lists commands for game \n"
            "quit - exits game")
            continue
        
        # If not an exit condition or 'help' the program will read the users input and determine how much they win
        else:
            # removes the text 'bet ' to isolate the users bets to be compared to the actual location
            user_input = re.sub('bet ', '', user_input)
            bets = user_input.split(", ")

            # If the location is not found within the list of bets, the loop does not continue to check each bet and prints the losing message, then allows user to continue
            if location[1] not in bets:
                print(location[0])
                print("You Lose!")
                location = ball_location.location()
                continue

            # For each bet in the list of bets, if the bet is equal to the exact location, the winning message will be displayed
            for bet in bets:
                bet = bet.split(" ")
                if bet[0] == location[1]:
                    winnings = int(bet[1]) * 35
                    print(location[0])   
                    print("Congratulations You Won $" + str(winnings))
                    location = ball_location.location()
                    break
    
def main():
    url = 'abcd.com'
    url = re.sub('\.com$', "", url)
    print(url)

if __name__ == '__main__':
    main()