import openai
import os
from dotenv import load_dotenv
from colorama import Fore, Back, Style


load_dotenv()

LANGUAGE_MODEL = "gpt-3.5-turbo-1106"
LANGUAGE_MODEL_GPT_4 = "gpt-4-1106-preview"
ASSISTANT_NAME = "Alex, Customer Support Agent"
ASSISTANT_DEFAULT_INSTRUCTIONS = """You are Alex. You are a customer support
agent at a company selling and repairing Washing Machines. Use the user manual
to answer the user's inquiries to the best of your abilities. If you don't
know the exact answer, give the customer support's email address."""

# Initialize clients with API keys
client = openai.OpenAI()

def create_assistant(file):
    """Creates an assistant with the default instructions."""
    pass

def create_thread():
    """Creates a thread."""
    pass

def add_message_to_thread(thread, file, message):
    """Adds a message to a thread."""
    pass

def run_assistant(thread, assistant):
    """Runs an assistant on a thread."""
    print_messages_from_thread

def check_status(thread_id, run_id):
    """Checks the status of a run every second until it is completed."""
    pass

def print_messages_from_thread(thread_id):
    """Prints all messages from a thread."""
    pass

def main():

    # Step 1 - Create an assistant

    # Step 2 - Create a thread

    print(Fore.CYAN + """Agent: Hello, I am Alex. I am here to assist you \n (type 'exit' to quit)""" + Fore.RESET)

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # Step 3 - Add a message to the thread
        
        # Step 4 - Run the Assistant

        # Step 5 - Check the run status

        # Step 6 - Pring the messages from the thread

if __name__ == "__main__":
    main()