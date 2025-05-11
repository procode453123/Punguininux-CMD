import time
import os
import random
import webbrowser
import turtle
import subprocess
from tkinter import messagebox  # Not used currently but imported for potential future use

def display_code_summary():
    """
    Displays a summary of the script's functionalities.
    """
    summary = """
    This script is a command interpreter called Punguininux. Here are its main features:
    - System commands: cd, mkdir, rm, ls, tree, pwd, etc.
    - File management: cat, touch, mv, start.
    - Games and drawings: Hangman game, drawing with turtle, interactive paint.
    - Information: version, system, creator, credits.
    - Utilities: echo, calc, internet, time, clear.
    - Menus: main menu and secondary menu.
    - Advanced features: network scanning, redirection to Windows Terminal.
    """
    print(summary)

# Constants
VERSION = "2.0"
DEFAULT_DIRECTORY = "c:\\"


def nmap_scan():
    """
    Performs a network scan using nmap if installed.
    """
    try:
        # Check if nmap is installed by attempting to run 'nmap -h'
        result = subprocess.run(["nmap", "-h"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            print("Error: Nmap is not installed on this computer.")
            return

        # Prompt user for target address
        target = input("Enter the target IP address or network (e.g., 192.168.1.0/24): ")
        print(f"Launching Nmap scan on {target}...")
        print("Please wait...")
        print("This operation may take some time.")
        subprocess.run(["nmap", target])
    except FileNotFoundError:
        print("Error: Nmap is not installed on this computer.")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_help_menu():
    """
    Displays a list of available commands with descriptions.
    """
    help_menu = {
        "help/?": "Display help",
        "exit/exit()": "Close Punguininux",
        "cmd/info": "Display information",
        "clear/cls": "Clear the screen",
        "pwd": "Show current directory",
        "echo <message>": "Display a message",
        "cd <directory>": "Change directory",
        "mkdir <folder_name>": "Create a folder",
        "version": "Show Punguininux version",
        "system/sys": "Display system information",
        "credit(s)": "Show credits",
        "createur": "Show creator",
        "internet/web": "Open Google in browser",
        "menu": "Display secondary menu",
        "scan": "Scan the network",
        "time/temps": "Show current time",
        "ls/dir": "List all files",
        "tree": "Display directory structure",
        "game/jeu": "Play Hangman game",
        "dessin": "Draw a shape",
        "paint": "Draw with cursor",
        "rm <file>": "Delete a file",
        "hello/bonjour": "Display welcome message",
        "mmmc": "Open an MMC",
        "console": "Open command prompt",
        "cat <file_name>": "Read a file",
        "touch <file_name>": "Create a new file",
        "mv <old_name> <new_name>": "Rename a file",
        "calc": "Perform calculations",
        "start <exe_file>": "Launch an executable (.exe)"
    }

    for command, description in help_menu.items():
        print(f"\033[36m{command}\033[0m - {description}")

def display_system_info():
    """
    Displays the operating system information.
    """
    os_name = os.name
    if os_name == "nt":
        print("Windows")
    elif os_name == "posix":
        print("Mac OS or Linux")
    else:
        print("Unknown OS")

def menu_loop():
    """
    Secondary menu loop for additional interactions.
    """
    while True:
        user_input = input(">>> ").lower()
        if user_input == "join":
            channel = random.randint(1, 9)
            print("Channel number", channel)
        elif user_input == "help":
            print("Welcome to the system menu, type 'return' or 'join' to go back.")
        elif user_input == "system":
            display_system_info()
        elif user_input == "return":
            main()
            break
        else:
            print("Invalid command.")

def play_hangman_game():
    """
    Implements a simple Hangman game.
    """
    words = [
    "python",       
    "computer",     
    "programming",  
    "hangman",      
    "game",        
    "word",        
    "command",     
    "terminal",    
    "linux",        
    "keyboard",     
    "monitor",      
    "developer",    
    "variable",    
    "function",     
    "loop",         
    "debug",        
    "google"       
]

    secret_word = random.choice(words)
    found_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print(f"The word to guess has {len(secret_word)} letters.")

    while attempts_left > 0:
        letter = input("Enter a letter: ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            continue

        if letter in found_letters:
            print("You already found this letter.")
            continue

        if letter in secret_word:
            found_letters.append(letter)
            print(f"Good job! The word contains the letter '{letter}'.")
        else:
            attempts_left -= 1
            print(f"The letter '{letter}' is not in the word. You have {attempts_left} attempts left.")

        displayed_word = "".join([char if char in found_letters else "_" for char in secret_word])
        print(f"Current word: {displayed_word}")

        if displayed_word == secret_word:
            print(f"Congratulations! You've guessed the word: {secret_word}")
            break

    if attempts_left == 0:
        print(f"Game over! The word was: {secret_word}")

def rename_file(old_name, new_name):
    """
    Renames a file from old_name to new_name.
    Returns success or error message.
    """
    try:
        os.rename(old_name, new_name)
        return f"File '{old_name}' has been renamed to '{new_name}'."
    except FileNotFoundError:
        return f"File '{old_name}' does not exist."
    except PermissionError:
        return "Permission error."

def draw_shape():
    """
    Draws a complex shape using turtle graphics.
    """
    turtle.penup()
    turtle.left(90)
    turtle.forward(200)
    turtle.pendown()
    turtle.right(90)

    
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(10, 180)
    turtle.circle(25, 110)
    turtle.left(50)
    turtle.circle(60, 45)
    turtle.circle(20, 170)
    turtle.right(24)
    turtle.forward(30)
    turtle.left(10)
    turtle.circle(30, 110)
    turtle.forward(20)
    turtle.left(40)
    turtle.circle(90, 70)
    turtle.circle(30, 150)
    turtle.right(30)
    turtle.forward(15)
    turtle.circle(80, 90)
    turtle.left(15)
    turtle.forward(45)
    turtle.right(165)
    turtle.forward(20)
    turtle.left(155)
    turtle.circle(150, 80)
    turtle.left(50)
    turtle.circle(150, 90)
    turtle.end_fill()

    
    turtle.left(150)
    turtle.circle(-90, 70)
    turtle.left(20)
    turtle.circle(75, 105)
    turtle.setheading(60)
    turtle.circle(80, 98)
    turtle.circle(-90, 40)

    turtle.left(180)
    turtle.circle(90, 40)
    turtle.circle(-80, 98)
    turtle.setheading(-83)

    
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(45)

    
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(-80, 90)
    turtle.right(90)
    turtle.circle(-80, 90)
    turtle.end_fill()

    
    turtle.right(135)
    turtle.forward(60)
    turtle.left(180)
    turtle.forward(85)
    turtle.left(90)
    turtle.forward(80)

    
    turtle.right(90)
    turtle.right(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(80, 90)
    turtle.left(90)
    turtle.circle(80, 90)
    turtle.end_fill()

    
    turtle.left(135)
    turtle.forward(60)
    turtle.left(180)
    turtle.forward(60)
    turtle.right(90)
    turtle.circle(200, 60)
    turtle.done()

def draw_with_cursor():
    """
    Allows drawing with arrow keys.
    """
    print("Paint [version 0.1]")
    print("Drawing with arrow keys!")

    def move(direction):
        """
        Moves the turtle in the specified direction.
        """
        directions = {"up": 90, "down": 270, "left": 180, "right": 0}
        turtle.setheading(directions[direction])
        turtle.forward(10)

    turtle.speed("fastest")
    turtle.listen()

    # Bind arrow keys to movement functions
    turtle.onkeypress(lambda: move("up"), "Up")
    turtle.onkeypress(lambda: move("down"), "Down")
    turtle.onkeypress(lambda: move("left"), "Left")
    turtle.onkeypress(lambda: move("right"), "Right")
    turtle.done()

def save_state():
    """
    Placeholder function for saving state.
    """
    pass  # Implement saving functionality if needed

def main():
    """
    Main program loop.
    """
    print(f"\033[37m[Version {VERSION}]\033[0m")
    print("\n\033[36m-----------------------------------\033[0m")
    print("\033[32mWelcome to Punguininux!\033[0m")
    print("\033[34mType 'help' to see available commands.\033[0m")
    print("\033[33mCreated by Caëlan\033[0m")
    print("\033[37mIn case of bugs, please send an email to: merlincaelan@gmail.com\033[0m")
    print("\n\033[36m-----------------------------------\033[0m")

    # Change to default directory
    os.chdir(DEFAULT_DIRECTORY)

    while True:
        try:
            user_input = input(f"{os.getcwd()}-$ ").lower()

            if user_input in ["help", "?"]:
                display_help_menu()

            elif user_input == "scan":
                nmap_scan()

            elif user_input.startswith("echo "):
                message = user_input.split("echo ", 1)[1]
                print(message)

            elif user_input.startswith("mkdir "):
                directory = user_input.split("mkdir ", 1)[1]
                try:
                    os.makedirs(directory)
                except FileExistsError:
                    print(f"The folder '{directory}' already exists.")

            elif user_input.startswith("start "):
                executable = user_input.split("start ", 1)[1]
                os.system(f"start {executable}")

            elif user_input.startswith("cd "):
                directory = user_input.split("cd ", 1)[1]
                try:
                    os.chdir(directory)
                except FileNotFoundError:
                    print("Error: Directory does not exist.")

            elif user_input.startswith("rm "):
                file = user_input.split("rm ", 1)[1]
                try:
                    os.remove(file)
                except FileNotFoundError:
                    print("Error: File does not exist.")
                except PermissionError:
                    print("Permission error.")

            elif user_input.startswith("cat "):
                file = user_input.split("cat ", 1)[1]
                file_path = os.path.join(os.getcwd(), file)
                try:
                    with open(file_path, 'r') as f:
                        print(f.read())
                except FileNotFoundError:
                    print("The specified file does not exist.")

            elif user_input.startswith("touch "):
                file = user_input.split("touch ", 1)[1]
                try:
                    with open(file, "w") as f:
                        pass
                except PermissionError:
                    print("Permission error.")

            elif user_input in ["exit", "exit()"]:
                print("\nThank you for using Penguininux. Goodbye!")
                save_state()
                time.sleep(2.5)
                break

            elif user_input.startswith("mv "):
                params = user_input.split("mv ", 1)[1].split()
                if len(params) != 2:
                    print("Usage: mv <old_name> <new_name>")
                else:
                    result = rename_file(params[0], params[1])
                    print(result)

            elif user_input == "":
                print("Please enter a command.")

            elif user_input in ["help version", "version"]:
                print(f"Your version is {VERSION}.")

            elif user_input in ["system", "sys"]:
                display_system_info()

            elif user_input == "credit":
                print("There are no credits for this software.")

            elif user_input == "createur":
                print("The creator of this software is Caëlan.")

            elif user_input == "menu":
                menu_loop()

            elif user_input == "pwd":
                print(os.getcwd())

            elif user_input in ["game", "jeu"]:
                play_hangman_game()

            elif user_input in ["internet", "web"]:
                webbrowser.open_new("https://google.com/")

            elif user_input in ["time", "temps"]:
                print(time.strftime("%H:%M:%S"))

            elif user_input in ["clear", "cls"]:
                os.system("cls" if os.name == "nt" else "clear")

            elif user_input in ["ls", "dir"]:
                for file in os.listdir():
                    print(file)

            elif user_input == "tree":
                os.system("tree")

            elif user_input == "dessin":
                draw_shape()

            elif user_input == "paint":
                draw_with_cursor()

            elif user_input in ["bonjour", "hello"]:
                print("Welcome to Punguininux.")

            elif user_input == "calc":
                try:
                    expression = input("Enter the expression to calculate: ")
                    result = eval(expression)
                    print(f"Result: {result}")
                except Exception as e:
                    print(f"Calculation error: {e}")

            else:
                print(f"Unknown command: {user_input}")

        except KeyboardInterrupt:
            # Exit gracefully on Ctrl+C
            break

if __name__ == "__main__":
    main()
    print("Thank you for using Penguininux. Goodbye!")
