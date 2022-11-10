import word_art
import ball_location
import commands

def main():
    print(word_art.welcome)
    location = ball_location.location()
    commands.command_prompts(location)

if __name__ == '__main__':
    main()