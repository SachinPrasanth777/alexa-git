import os
import time
import random
import shutil  # To get terminal size for centering text
import pygame

# Initialize the pygame mixer for background music
pygame.mixer.init()

# Path to assets folder and music file
ASSETS_PATH = "assets"
MUSIC_FILE = os.path.join(ASSETS_PATH, "background.mp3")
CREDITS = "Background music: 'Thinking Bout You' by TogoBoiTen"
HEART = "♥"

# Header text to display at the top
HEADER = """
███╗   ███╗ █████╗ ████████╗██╗  ██╗    ███████╗██╗   ██╗██╗███████╗
████╗ ████║██╔══██╗╚══██╔══╝██║  ██║    ██╔════╝██║   ██║██║██╔════╝
██╔████╔██║███████║   ██║   ███████║    █████╗  ██║   ██║██║█████╗  
██║╚██╔╝██║██╔══██║   ██║   ██╔══██║    ██╔══╝  ╚██╗ ██╔╝██║██╔══╝  
██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║    ███████╗ ╚████╔╝ ██║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚══════╝  ╚═══╝  ╚═╝╚══════╝

Solve math questions to keep your lives. 
Type 'exit' to quit or 'restart' to start over.
🎵 {credits} 🎵
""".format(credits=CREDITS)


def center_text(text):
    """Centers the given text based on terminal width."""
    columns = shutil.get_terminal_size().columns
    return "\n".join(line.center(columns) for line in text.splitlines())


def clear_screen():
    """Clears the console based on the OS and prints the header."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/Mac
        os.system('clear')
    print(center_text(HEADER))


def play_background_music():
    """Play the background music from the assets folder with low volume."""
    if os.path.exists(MUSIC_FILE):
        pygame.mixer.music.load(MUSIC_FILE)
        pygame.mixer.music.set_volume(0.4)  # Set the music volume to a low level for background effect
        pygame.mixer.music.play(-1)  # Loop the music indefinitely
    else:
        print("Background music file not found. Continuing without music.")


def display_lives(lives):
    """Display the remaining lives using heart symbols."""
    hearts = HEART * lives
    print(center_text(f"Lives: {hearts}\n"))


def start_quiz_game():
    """Start the math quiz game and handle the game flow."""
    play_background_music()
    
    while True:
        clear_screen()
        
        lives = 5
        score = 0
        
        while lives > 0:
            clear_screen()
            display_lives(lives)
            
            # Generate a math question
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            operator = random.choice(['+', '-', '*'])
            question = f"{num1} {operator} {num2}"
            correct_answer = eval(question)  # Use eval to evaluate the math expression
            
            print(center_text(f"🔢 Question: {question} = ?"))
            user_input = input("Your Answer: ")

            # Handle exit or restart commands
            if user_input.lower() == 'exit':
                print(center_text("👋 Exiting the game. Thanks for playing!"))
                pygame.mixer.music.stop()
                return
            elif user_input.lower() == 'restart':
                print(center_text("🔄 Restarting the game..."))
                time.sleep(1)
                break
            elif user_input.isdigit() and int(user_input) == correct_answer:
                score += 1
                print(center_text("✅ Correct! Great job!\n"))
            else:
                lives -= 1
                print(center_text(f"❌ Incorrect! The correct answer was {correct_answer}."))
                print(center_text(f"Lives remaining: {lives}\n"))
            
            time.sleep(1)

        # Game over scenario
        if lives == 0:
            clear_screen()
            print(center_text("💀 Game Over! You ran out of lives. 💀"))
            print(center_text(f"🎯 Your final score: {score}\n"))

        # Ask if the player wants to play again
        play_again = input(center_text("Would you like to play again? (yes/no): ")).lower()
        if play_again != 'yes':
            print(center_text("👋 Thanks for playing! Goodbye!"))
            pygame.mixer.music.stop()
            break


if __name__ == "__main__":
    start_quiz_game()
