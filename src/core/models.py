from rich import print as rprint
from typing import List, Optional
import cli.interface
import json
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
        self.role_dict = {}

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
            
     




    def add_role(self, role: str, status: bool):
        self.role_dict.update({role:status})

    def save_role_dict(self):
        # Serializing json
        
        json_object = json.dumps(self.role_dict, indent=len(self.role_dict))

        # Writing to sample.json
        with open("test.json", "w") as outfile:
            outfile.write(json_object)
      





    def run_setup(self):
        # prompt
        print("-------------------------------------------")
        
        slow("What can I call you?", 0.03, True)
        user_input = input()
        self.add_role(user_input, True)
        
        slow("Are you a follower of Christ?", 0.03, True)
        user_input = input()
        if user_input.lower() in ("y", "yes"):
            self.add_role("Christ follower", True)
            slow("That's great to hear! I made this tool specifically so that people like us can structure our lives to better serve him!", 0.03, True)
        # write user_input
        elif user_input.lower() in ("n", "no"):
            self.add_role("Christ follower", False)
            slow("Thanks for sharing. I just want you to know that Jesus loves you, and that if you're lost in the toxic world of self-improvement HE can legitimately rescue you from it - if you let him.", 0.03, True)
            slow("John 3:16 says: 'For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life.", 0.03, True)
            slow("Anyway ~", 0.03, True)
        # write user_input
        slow("Are you married or in a serious relationship?", 0.03, True)
        user_input = input()
        if user_input.lower() in ("y", "yes"):
            slow("Which one? (type 'married' or 'relationship')", 0.03, True)
            user_input = input()
            self.add_role(user_input, True)
        
        elif user_input.lower() in ("married", "relationship", "serious relationship"):
            
            self.add_role(user_input, True)

        elif user_input.lower() in ("n", "no"):
            slow("Got it.", 0.03, True)
            self.add_role("Married", False)

        slow("Do you have living relatives?", 0.03, True)
        user_input = input()

        if user_input.lower() in ("yes", "y"):
            slow("That's great to hear", 0.03, True)
            self.add_role("Living Relatives", True)
            
        elif user_input.lower() in ("n", "no"):
            slow("I'm sorry to hear that :/", 0.03, True)
            self.add_role("Living Relatives", False)
            

        slow("Do you have any friends?", 0.03, True)
        user_input = input()
        
        if user_input.lower() in ("yes", "y"):
            slow("Wonderful!", 0.03, True)
            self.add_role("Friends", True)

        elif user_input.lower() in ("n", "no"):
            slow("Oof.", 0.03, True)
            self.add_role("Friends", False)


        slow("Do you work a job?", 0.03, True)
        user_input = input()

        if user_input.lower() in ("yes", "y"):
            slow("Nice!", 0.03, True)
            self.add_role("Job", True)

        elif user_input.lower() in ("n", "no"):
            slow("Okay.", 0.03, True)
            self.add_role("Job", False)

        slow("Are you a student?", 0.03, True)
        user_input = input()

        if user_input.lower() in ("yes", "y"):
            slow("Cool!", 0.03, True)
            self.add_role("Student", True)

        elif user_input.lower() in ("n", "no"):
            slow("Got it.", 0.03, True)
            self.add_role("Student", False)

        slow("Do you have any side projects, or things that you're passionate about?", 0.03, True)
        user_input = input()
        if user_input.lower() in ("yes", "y"):
            slow("What are they? (type '0' when you're finished)", 0.03, True)
            val = True
            while val == True:
                user_input = input()
                if user_input == "0":
                    val = False
                else:
                    # write user_input
                    
                    self.add_role(user_input, True)
                    slow("Got it, what else?", 0.03, True)

            # write user_input
        elif user_input.lower() in ("n", "no"):
            slow("Perfect, that makes my life easier!", 0.03, True)
            self.add_role("Hobbies", False)
            
        print(self.role_dict)
        self.save_role_dict()
        self.run()
        

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
    
