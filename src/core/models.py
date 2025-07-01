from rich import print as rprint
from typing import List, Optional
import cli.interface
from tabulate import tabulate
from datetime import datetime
import os
import json
from utils.stuff import slow_type as slow
from core import task_database

gigachad_art = ":)"

"""
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


class Commitment:
    def __init__(self, title: str, category: str, duration_minutes: Optional[int] = None, priority: int = 1, start_time: Optional[str] = None):
        self.title = title
        self.category = category
        self.duration = duration_minutes
        self.start_time = start_time
        self.frequency_per_week = 0


    def __repr__(self):
        return (f"Commitment(title='{self.title}', duration={self.duration_minutes}, "
                f"priority={self.priority}, start_time={self.start_time}, category={self.category})")
    


class Task:
    def __init__(self, title, duration, priority_level, category):
        self.title = title
        self.duration = duration
        self.priority_level = priority_level
        self.category = category

class RoleManager: # All of the main program functions
    def __init__(self, username: Optional[str] = None):
        self.roles = []
        self.username = username
        self.role_dict = {}
        self.main_loop = True

    def run(self): # WHAT ACTUALLY HAPPENS
        cli.interface.clear_screen()
        print("Welcome back to \nR. O. L. E. S.\n-------------------------------------------\n")
        slow(gigachad_art, 0.01, True)
        self.load_roles()
        #where the rest of the program takes place
        while self.main_loop == True:

            slow(f"What would you like to do today {self.role_dict['Username']}?", 0.03, True)
            slow("1. Generate Today's Schedule", 0.03, True)
            slow("2. Update Roles", 0.03, True)
            slow("3. New Commitment", 0.03, True)
            user_input = input()
            if user_input == "1":
                self.generate_schedule()
            elif user_input == "2":
                self.run_setup()            

    def load_roles(self):
        if os.path.exists("user_profile.json"):

            with open('user_profile.json', 'r') as file:
                self.role_dict = json.load(file)
                self.display_roles()
            
        else:
            slow("Looks like you're a first time user!", 0.03, True)
            slow("Run initial setup?", 0.03, True)
            yes_no = input()
            if yes_no.lower() in ("y", "yes"):
                self.run_setup()
            else:
                print("bruh")


    def display_roles(self):
        rprint("[bold green]Your roles are:[/bold green]")
        self.username = self.role_dict["Username"]
        for role in self.role_dict:

            if self.role_dict[role] == True:

                slow(f"  - {role}", 0.03, True)
                print("-------------------------------------------")

            
            
    

    def add_role(self, role: str, status: bool):
        self.role_dict.update({role:status})

    def save_role_dict(self):
        # Serializing json
        
        json_object = json.dumps(self.role_dict, indent=len(self.role_dict))

        # Writing to sample.json
        with open("user_profile.json", "w") as outfile:
            outfile.write(json_object)
      

    def run_setup(self):
        # prompt
        cli.interface.clear_screen()
        print("-------------------------------------------")
        
        slow("What can I call you?", 0.03, True)
        user_input = input()
        self.add_role("Username", user_input)
        
        slow("Are you a follower of Christ?", 0.03, True)
        user_input = input()
        if user_input.lower() in ("y", "yes"):
            self.add_role("Christ Follower", True)
            slow("That's great to hear! I made this tool specifically so that people like us can structure our lives to better serve him!", 0.03, True)
        
        elif user_input.lower() in ("n", "no"):
            self.add_role("Christ Follower", False)
            slow("Thanks for sharing. I just want you to know that Jesus loves you, and that if you're lost in the toxic world of self-improvement HE can legitimately rescue you from it - if you let him.", 0.03, True)
            slow("John 3:16 says: 'For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life.", 0.03, True)
            slow("Anyway ~", 0.03, True)
       
       # FIXME: KNOWN BUG WITH INPUT
        slow("Are you married or in a serious relationship?", 0.03, True)
        user_input = input()
        if user_input.lower() in ("y", "yes"):
           # slow("Which one? (type 'married' or 'relationship')", 0.03, True)
           # user_input = input()
            self.add_role("Partner", True)
        
        elif user_input.lower() in ("married", "relationship", "serious relationship"):
            
            self.add_role("Partner", True)

        elif user_input.lower() in ("n", "no"):
            slow("Got it.", 0.03, True)
            self.add_role("Partner", False)

        slow("Do you have living relatives?", 0.03, True)
        user_input = input()

        if user_input.lower() in ("yes", "y"):
            slow("That's great to hear", 0.03, True)
            self.add_role("Relative", True)
            
        elif user_input.lower() in ("n", "no"):
            slow("I'm sorry to hear that :/", 0.03, True)
            self.add_role("Relative", False)
            

        slow("Do you have any friends?", 0.03, True)
        user_input = input()
        
        if user_input.lower() in ("yes", "y"):
            slow("Wonderful!", 0.03, True)
            self.add_role("Friend", True)

        elif user_input.lower() in ("n", "no"):
            slow("Oof.", 0.03, True)
            self.add_role("Friend", False)


        slow("Do you work a job?", 0.03, True)
        user_input = input()

        if user_input.lower() in ("yes", "y"):
            slow("Nice!", 0.03, True)
            self.add_role("Employee", True)

        elif user_input.lower() in ("n", "no"):
            slow("Okay.", 0.03, True)
            self.add_role("Employee", False)

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

    #def check_commitments(self, schedule: list):
        # load list of commitments
        # check if time (schedule[0][0])'s conflict
        # reorganize it

    def generate_schedule(self):

        import core.task_database as task_database
        cli.interface.clear_screen()
        start_time = datetime.now()
        schedule = []

        # A BEDTIME IS JUS TA COMMITMENT
        bedtime_hour = input("What hour would you like to go to bed by tonight?\n")
        bedtime_minute = input("What minute?\n")
        bedtime_AM_PM = input("AM or PM?\n")
        

        
        
        cli.interface.clear_screen()

        # Initial time setup
        hour = start_time.hour
        minute = start_time.minute
        AM_PM = "AM"

        if hour >= 12:
            AM_PM = "PM"
            if hour > 12:
                hour -= 12
        elif hour == 0:
            hour = 12  # midnight

        current_hour = hour
        current_minute = minute

        for role in self.role_dict.keys():
            task_count = 1
            if self.role_dict[role] == True:
                role_name = [role]

                # for role category in task_dict

                for role_category in task_database.task_dict.values():
                
                    # for specific task in task_dict
                
                    for task_attribute in role_category.values():
                        
                                            
                        if role_name[0] == task_attribute["category"]:

                        

                        
                            task = Task(task_attribute["name"], task_attribute["duration"], task_attribute["priority"], task_attribute["category"])

                            # Build readable time
                            readable_time = f'{current_hour}:{str(current_minute).zfill(2)} {AM_PM}'
                              
                            

                            schedule.append([readable_time, task.title, task.category])
                                

                            task_count += 1

                            # Update minute
                            current_minute += task.duration

                            # Handle overflow
                            while current_minute >= 60:
                                current_minute -= 60
                                current_hour += 1
                                if current_hour == 12:
                                    AM_PM = "PM" if AM_PM == "AM" else "AM"
                                elif current_hour > 12:
                                    current_hour -= 12
        


        readable_bedtime = f'{bedtime_hour}:{str(bedtime_minute).zfill(2)} {bedtime_AM_PM}'
        bedtime = Commitment("Bedtime", "Human", readable_bedtime)
        schedule.append([readable_bedtime, bedtime.title, bedtime.category])
        print(schedule)
        
        # full_schedule = check_commitments(schedule)
                            
                            # needs to be a commitments LIST
                            # checks to see if readable time clashes with commitment time
                            # returns the updated schedule, reorganized to be inline with given priority values

        # schedule.append([readable_bedtime, task.title, task.category])
        print(tabulate(schedule, headers=["Time", "Activity", "Role"], tablefmt="fancy_grid"))
        exit()



    def __repr__(self):
        return(f"RoleManager(username='{self.username}')")



class Role:
    def __init__(self, name: str, commitments: Optional[List[Commitment]] = None): 
        self.name = name
        self.commitments = commitments if commitments else []

    def __repr__(self):
        return(f"Role(name='{self.name}', commitments={self.commitments})")
    
