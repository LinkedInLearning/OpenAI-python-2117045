import openai
import os
from dotenv import load_dotenv
from colorama import Fore, Back, Style


load_dotenv()

LANGUAGE_MODEL = "gpt-3.5-turbo-1106"
LANGUAGE_MODEL_GPT_4 = "gpt-4-1106-preview"
LANGUAGE_MODEL_GPT_4_PREVIEW = "gpt-4-turbo-preview"
ASSISTANT_NAME = "Alex, Agent Support à la Clientèle"
ASSISTANT_DEFAULT_INSTRUCTIONS = """Vous êtes Alex, un agent du support clientèle capable de répondre aux demandes des utilisateurs du mieux que vous le pouvez."""

# Initialize clients with API keys
client = openai.OpenAI()

def create_assistant():
    """Creates an assistant with the default instructions."""
    assistant = client.beta.assistants.create(
        name=ASSISTANT_NAME ,
        instructions=ASSISTANT_DEFAULT_INSTRUCTIONS,
        model=LANGUAGE_MODEL_GPT_4_PREVIEW,
    )
    print(assistant)
    return assistant

def create_thread():
    """Creates a thread."""
    thread = client.beta.threads.create()
    print(thread)
    return thread

def add_message_to_thread(thread, message):
    """Adds a message to a thread."""
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message
    )
    print(message)

def run_assistant(thread, assistant):
    """Runs an assistant on a thread."""
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id
    )
    print(f"Run: {run.id}")
    return run

def check_status(thread_id, run_id):
    """Checks the status of a run every second until it is completed."""
    pass

def print_messages_from_thread(thread_id):
    """Prints all messages from a thread."""
    pass

def main():

    # Step 1 - Create an assistant
    assistant = create_assistant()

    # Step 2 - Create a thread
    thread = create_thread()

    print(Fore.CYAN + "Agent: Bonjour, je suis Alex. Je suis ici pour vous aider \n(tapez 'exit' pour quitter)" + Fore.RESET)

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # Step 3 - Add a message to the thread
        add_message_to_thread(thread, user_input)
        
        # Step 4 - Run the Assistant
        run = run_assistant(thread, assistant)

        # Step 5 - Check the run status

        # Step 6 - Pring the messages from the thread

if __name__ == "__main__":
    main()