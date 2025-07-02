from core.role_manager import RoleManager
import os
import sys
import time


def run_cli():
    manager = RoleManager()
    manager.run()  # calls the actual app code


def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')



def slow_type(text: str, delay: float = 0.03, newline: bool = True):
    """
    Prints text to the console one character at a time.

    Args:
        text (str): The text to print.
        delay (float): Delay between characters in seconds (default is 0.03).
        newline (bool): Whether to add a newline at the end (default is True).
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()  # Move to the next line
