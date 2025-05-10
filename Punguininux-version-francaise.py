import time
import os
import random
import webbrowser
import turtle
import subprocess
from tkinter import messagebox  #not used in the current code but imported for potential future use
def display_code_summary():
    summary = """
    Ce script est un interpréteur de commandes appelé Punguininux. Voici un résumé des fonctionnalités principales :
    - Commandes système : cd, mkdir, rm, ls, tree, pwd, etc.
    - Gestion de fichiers : cat, touch, mv, start.
    - Jeux et dessins : jeu du pendu, dessin avec turtle, paint interactif.
    - Informations : version, system, createur, credits.
    - Utilitaires : echo, calc, internet, time, clear.
    - Menus : menu principal et menu secondaire.
    - Fonctionnalités avancées : scan réseau, redirection vers Windows Terminal.
    """
    print(summary)
# Constants
VERSION = "2.0"
DEFAULT_DIRECTORY = "c:\\"


def nmap_scan():
    try:
        # Check if nmap is installed
        result = subprocess.run(["nmap", "-h"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            print("Erreur : Nmap n'est pas installé sur cet ordinateur.")
            return

        # Perform a network scan
        target = input("Entrez l'adresse IP ou le réseau cible (ex: 192.168.1.0/24) : ")
        print(f"Lancement du scan Nmap sur {target}...")
        print("Veuillez patienter...")
        print("Cette opération peut prendre un certain temps.")
        subprocess.run(["nmap", target])
    except FileNotFoundError:
        print("Erreur : Nmap n'est pas installé sur cet ordinateur.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def display_help_menu():
    help_menu = {
        "help/?": "afficher l'aide",
        "exit/exit()": "fermer Punguininux",
        "cmd/info": "afficher les informations",
        "clear/cls": "effacer l'écran",
        "pwd": "afficher le répertoire actuel",
        "echo <message>": "afficher un message",
        "cd <répertoire>": "changer le répertoire",
        "mkdir <nom-dossier>": "créer un dossier",
        "version": "afficher la version de Punguininux",
        "system/sys": "afficher le système",
        "credit(s)": "afficher les crédits",
        "createur": "afficher le créateur",
        "internet/web": "ouvrir Google",
        "menu": "afficher un menu secondaire",
        "scan": "scanner le réseau",
        "time/temps": "afficher l'heure",
        "ls/dir": "afficher tous les fichiers",
        "tree": "afficher la structure de fichiers",
        "game/jeu": "jouer à un jeu (le jeu du pendu)",
        "dessin": "voir un dessin",
        "paint": "dessiner avec un curseur",
        "rm <fichier>": "supprimer des fichiers",
        "hello/bonjour": "afficher la page d'accueil",
        "mmmc": "ouvrir un MMC",
        "console": "ouvrir un cmd (invite de commande)",
        "cat <nom_fichier>": "lire des fichiers",
        "touch <nom_fichier>": "créer des fichiers",
        "mv <ancien_nom> <nouveau_nom>": "changer le nom d'un fichier",
        "calc": "faire des calculs",
        "start <fichier exe>": "lancer un fichier executable (.exe)"
    }

    for command, description in help_menu.items():
        print(f"\033[36m{command}\033[0m - {description}")

def display_system_info():
    os_name = os.name
    if os_name == "nt":
        print("Windows")
    elif os_name == "posix":
        print("Mac OS ou Linux")

def menu_loop():
    while True:
        user_input = input(">>> ").lower()
        if user_input == "join":
            canal = random.randint(1, 9)
            print("Canal numéro", canal)
        elif user_input == "help":
            print("Bienvenue dans le menu tape system, retour ou join")
        elif user_input == "system":
            display_system_info()
        elif user_input == "retour":
            main()
            break
        else:
            print("Commande invalide")

def play_hangman_game():
    words = ["python", "ordinateur", "programmation", "pendu", "jeu", "mot", "cmd", "idc", "copylinux", "nul", "bravo",
             "ghghg", "caveriendire", "impossible45645645642149631541614634136", "google"]
    secret_word = random.choice(words)
    found_letters = []
    attempts_left = 6

    print("Bienvenue au jeu du Pendu !")
    print(f"Le mot à deviner contient {len(secret_word)} lettres.")

    while attempts_left > 0:
        letter = input("Entrez une lettre : ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Veuillez entrer une seule lettre.")
            continue

        if letter in found_letters:
            print("Vous avez déjà trouvé cette lettre.")
            continue

        if letter in secret_word:
            found_letters.append(letter)
            print(f"Bien joué ! Le mot contient la lettre '{letter}'.")
        else:
            attempts_left -= 1
            print(f"La lettre '{letter}' ne fait pas partie du mot. Il vous reste {attempts_left} essais.")

        displayed_word = "".join([letter if letter in found_letters else "_" for letter in secret_word])
        print(f"Mot actuel : {displayed_word}")

        if displayed_word == secret_word:
            print(f"Bravo ! Vous avez trouvé le mot : {secret_word}")
            break

    if attempts_left == 0:
        print(f"Dommage ! Le mot était : {secret_word}")

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        return f"Le fichier '{old_name}' a été renommé en '{new_name}'."
    except FileNotFoundError:
        return f"Le fichier '{old_name}' n'existe pas."
    except PermissionError:
        return "Erreur de Permission"

def draw_shape():
    turtle.penup()
    turtle.left(90)
    turtle.fd(200)
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
    turtle.fd(30)
    turtle.left(10)
    turtle.circle(30, 110)
    turtle.fd(20)
    turtle.left(40)
    turtle.circle(90, 70)
    turtle.circle(30, 150)
    turtle.right(30)
    turtle.fd(15)
    turtle.circle(80, 90)
    turtle.left(15)
    turtle.fd(45)
    turtle.right(165)
    turtle.fd(20)
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

    turtle.fd(30)
    turtle.left(90)
    turtle.fd(25)
    turtle.left(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(-80, 90)
    turtle.right(90)
    turtle.circle(-80, 90)
    turtle.end_fill()
    turtle.right(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(85)
    turtle.left(90)
    turtle.fd(80)

    turtle.right(90)
    turtle.right(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(80, 90)
    turtle.left(90)
    turtle.circle(80, 90)
    turtle.end_fill()
    turtle.left(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(60)
    turtle.right(90)
    turtle.circle(200, 60)
    turtle.done()

def draw_with_cursor():
    print("paint [version 0.1]")
    print("Dessin avec les flèches du clavier !")

    def move(direction):
        directions = {"up": 90, "down": 270, "left": 180, "right": 0}
        turtle.setheading(directions[direction])
        turtle.forward(10)

    turtle.speed("fastest")
    turtle.listen()

    turtle.onkeypress(lambda: move("up"), "Up")
    turtle.onkeypress(lambda: move("down"), "Down")
    turtle.onkeypress(lambda: move("left"), "Left")
    turtle.onkeypress(lambda: move("right"), "Right")
    turtle.done()

def save_state():
    pass

def main():
    print(f"\033[37m[Version {VERSION}]\033[0m")
    print("\n\033[36m-----------------------------------\033[0m")
    print("\033[32mBienvenue sur Punguininux !\033[0m")
    print("\033[34mTapez 'help' pour afficher les commandes disponibles.\033[0m")
    print("\033[33mCréé par Caëlan\033[0m")
    print("\033[37mEn cas de bug, merci d'envoyer un mail à l'adresse suivante : merlincaelan@gmail.com\033[0m")
    print("\n\033[36m-----------------------------------\033[0m")

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
                    print(f"Le dossier '{directory}' existe déjà.")
            elif user_input.startswith("start "):
                executable = user_input.split("start ", 1)[1]
                os.system(f"start {executable}")
            elif user_input.startswith("cd "):
                directory = user_input.split("cd ", 1)[1]
                try:
                    os.chdir(directory)
                except FileNotFoundError:
                    print("Erreur : Le Répertoire n'existe pas.")
            elif user_input.startswith("rm "):
                file = user_input.split("rm ", 1)[1]
                try:
                    os.remove(file)
                except FileNotFoundError:
                    print("Erreur : Le fichier n'existe pas.")
                except PermissionError:
                    print("Erreur de Permission.")
            elif user_input.startswith("cat "):
                file = user_input.split("cat ", 1)[1]
                file_path = os.path.join(os.getcwd(), file)
                try:
                    with open(file_path, 'r') as f:
                        print(f.read())
                except FileNotFoundError:
                    print("Le fichier spécifié n'existe pas.")
            elif user_input.startswith("touch "):
                file = user_input.split("touch ", 1)[1]
                try:
                    with open(file, "w") as f:
                        pass
                except PermissionError:
                    print("Erreur de Permission.")
            elif user_input in ["exit", "exit()"]:
                print("\nMerci d'avoir utilisé Penguininux. Au revoir!")
                save_state()
                time.sleep(2.5)
                break
            elif user_input.startswith("mv "):
                params = user_input.split("mv ", 1)[1].split()
                if len(params) != 2:
                    print("Utilisation : mv <ancien_nom> <nouveau_nom>")
                else:
                    result = rename_file(params[0], params[1])
                    print(result)
            elif user_input == "":
                print("Entrez une commande.")
            elif user_input in ["help version", "version"]:
                print(f"Votre version est la version {VERSION}.")
            elif user_input in ["system", "sys"]:
                display_system_info()
            elif user_input == "credit":
                print("Il n'y a pas de crédit pour ce logiciel.")
            elif user_input == "createur":
                print("Le créateur du logiciel est Caëlan.")
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
                print("Bienvenue dans Punguininux.")
            elif user_input == "calc":
                try:
                    expression = input("Entrez l'expression à calculer : ")
                    result = eval(expression)
                    print(f"Résultat : {result}")
                except Exception as e:
                    print(f"Erreur de calcul : {e}")
            else:
                print(f"Commande inconnue : {user_input}")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
    print("Merci d'avoir utilisé Penguininux. Au revoir!")
