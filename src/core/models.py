from rich import print as rprint
from typing import List, Optional
import cli.interface
from utils.stuff import slow_type as slow

gigachad_art = """
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠋⠉⠈⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⠀
⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⠀
⣿⣿⣿⣿⡏⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⠀
⣿⣿⣿⢏⣴⣿⣷⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⠀
⣿⣿⣟⣾⣿⡟⠁⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⢢⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀
⣿⣿⣿⣿⣟⠀⡴⠄⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣿⠀
⣿⣿⣿⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢴⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿⠀
⣿⣁⡀⠀⠀⢰⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡄⠀⣴⣶⣿⡄⣿⠀
⣿⡋⠀⠀⠀⠎⢸⣿⡆⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠗⢘⣿⣟⠛⠿⣼⠀
⣿⣿⠋⢀⡌⢰⣿⡿⢿⡀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣧⢀⣼⠀
⣿⣿⣷⢻⠄⠘⠛⠋⠛⠃⠀⠀⠀⠀⠀⢿⣧⠈⠉⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⣿⠀
⣿⣿⣧⠀⠈⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⢀⢃⠀⠀⢸⣿⣿⣿⣿⠀
⣿⣿⡿⠀⠴⢗⣠⣤⣴⡶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡸⠀⣿⣿⣿⣿⠀
⣿⣿⣿⡀⢠⣾⣿⠏⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⣿⣿⣿⣿⠀
⣿⣿⣿⣧⠈⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠀
⣿⣿⣿⣿⡄⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⠀
⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠙⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠁⠀⠀⠹⣿⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⣿⣿⣿⣿⠿⠛⠉⠉⠁⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⢀⠈⣿⣿⡿⠉⠛⠛⠛⠉⠉⠀⠀
"""

class RoleManager: # All of the main program functions
    def __init__(self, username: Optional[str] = None):
        self.roles = []
        self.username = username

    def run(self): # WHAT ACTUALLY HAPPENS
        cli.interface.clear_screen()
        print("Welcome back to \nR. O. L. E. S.\n-------------------------------------------\n")
        slow(gigachad_art, 0.01, True)
        self.load_roles()
        

    def load_roles(self):
        self.roles = []
        if self.roles == []:
            slow("Looks like you're a first time user!", 0.03, True)
            slow("Run initial setup?", 0.03, True)
            yes_no = input()
            if yes_no.lower() in ("y", "yes"):
                self.run_setup()
            else:
                print("bruh")
        else:
            self.display_roles()

    def display_roles(self):
        rprint("[bold green]Your roles are:[/bold green]")
        for role in self.roles:
            print(f"  - {role}")

    def run_setup(self):
        # prompt
        print("-------------------------------------------")
        # write user_input to json file
        slow("What can I call you?", 0.03, True)
        user_input = input()
        # write user_input
        slow("Are you a follower of Christ?", 0.03, True)
        user_input = input()
        if user_input.lower() in ("y", "yes"):
            slow("That's great to hear! I made this tool specifically so that people like us can structure our lives to better serve him!", 0.03, True)
        # write user_input
        elif user_input.lower() in ("n", "no"):
            slow("Thanks for sharing. I just want you to know that Jesus loves you, and that if you're lost in the toxic world of self-improvement HE can legitimately rescue you from it - if you let him.", 0.03, True)
            slow("John 3:16 says: 'For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life.", 0.03, True)
            slow("Anyway ~", 0.03, True)
        # write user_input
        slow("Are you married or in a serious relationship?", 0.03, True)
        user_input = input()
        if user_input.lower() in ("y", "yes"):
            slow("Which one? (type 'married' or 'relationship')", 0.03, True)
            user_input = input()
            # write user_input
        elif user_input.lower() in ("married", "relationship", "serious relationship"):
            user_input = input()
            # write user_input

        slow("Do you have living relatives?", 0.03, True)
        user_input = input()
        # write user_input

        if user_input.lower() in ("yes", "y"):
            print("nice")
            # write user_input
        elif user_input.lower() in ("n", "no"):
            print("nice")
            # write user_input

        slow("Do you have any friends?", 0.03, True)
        user_input = input()
        # write user_input

        slow("Do you work a job?", 0.03, True)
        user_input = input()
        # write user_input

        slow("Are you a student?", 0.03, True)
        user_input = input()
        # write user_input

        slow("Do you have any side projects, or things that you're passionate about?", 0.03, True)
        user_input = input()
        if user_input.lower() in ("yes", "y"):
            slow("What are they? (type '0' when you're finished)", 0.03, True)
            while True:
                user_input = input()
                if user_input == "0":
                    return False
                else:
                    # write user_input
                    print("Got it, what else?")

            # write user_input
        elif user_input.lower() in ("n", "no"):
            print("nice")
            # write user_input
        # write user_input

        

    def __repr__(self):
        return(f"RoleManager(username='{self.username}')")


class Commitment:
    def __init__(self, title: str, duration_minutes: Optional[int] = None, priority: int = 1, start_time: Optional[str] = None):
        self.title = title
        self.duration = duration_minutes
        self.start_time = start_time
        self.frequency_per_week = 0

    def __repr__(self):
        return (f"Commitment(title='{self.title}', duration={self.duration_minutes}, "
                f"priority={self.priority}, start_time={self.start_time})")
    

class Role:
    def __init__(self, name: str, commitments: Optional[List[Commitment]] = None): 
        self.name = name
        self.commitments = commitments if commitments else []

    def __repr__(self):
        return(f"Role(name='{self.name}', commitments={self.commitments})")
    
