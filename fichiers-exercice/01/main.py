import openai
import tiktoken
from colorama import Fore
from dotenv import load_dotenv


# Load the environment variables - set up the OpenAI API client
load_dotenv()


# Set up the model and prompt
LANGUAGE_MODEL = "gpt-3.5-turbo"
PROMPT_TEST = "This is a test prompt. Say this is a test"


def start():
    print(Fore.GREEN + "\nMENU")
    print("====")
    print("[1]- Poser une question à l'IA" )
    print("[2]- Quitter" + Fore.RESET)
    choice = input("Sélectionner: ")
    if choice == "1":
        ask()
    elif choice == "2":
        exit()
    else:
        print("Invalid choice")


def ask():
    """Poser une question pour générer une réponse de l'IA."""
    instructions = (
        "Presser ENTREE. Tapper 'x' pour revenir au menu principal."
    )
    print(Fore.BLUE + "\n\x1B[3m" + instructions + "\x1B[0m" + Fore.RESET)
    print("=================================================")

    while True:
        user_input = input("Q: ")

        # Exit
        if user_input == "x":
            start()
        else:
            # completion
            print(Fore.BLUE + f"A: " + Fore.RESET)
            print(Fore.WHITE + "\n-------------------------------------------------")


if __name__ == "__main__":
    start()
