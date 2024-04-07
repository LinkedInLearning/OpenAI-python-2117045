import openai
import tiktoken
from colorama import Fore
from dotenv import load_dotenv


# Load the environment variables - set up the OpenAI API client
load_dotenv()
client = openai.OpenAI()


# Set up the model and prompt
LANGUAGE_MODEL = "gpt-3.5-turbo"
PROMPT_TEST = "This is a test prompt. Say this is a test"
messages = [{"role": "system", "content": "You are helpful assistant."},]

def get_tokens(user_input: str):
    """Returns the number of tokens in a text string."""

    encoding = tiktoken.get_encoding("cl100k_base")

    token_integers = encoding.encode(user_input)
    tokens_usage = len(token_integers)

    tokenized_input = tokenized_input = list(
        map(
            lambda x: encoding.decode_single_token_bytes(x).decode("utf-8"),
            encoding.encode(user_input),
        )
    )
    print(f"{encoding}: {tokens_usage} tokens")
    print(f"token integers: {tokens_usage}")
    print(f"token bytes: {tokenized_input}")
    

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
            messages.append({"role": "user", "content": user_input})

            completion = client.chat.completions.create(
                model=LANGUAGE_MODEL,
                messages=messages, 
            )

            # print(completion.choices[0].message)

            print(Fore.BLUE + f"A: {completion.choices[0].message.content}" + Fore.RESET)
            print(Fore.WHITE + "\n-------------------------------------------------")


if __name__ == "__main__":
    start()
