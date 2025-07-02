from rich import print as rprint
from typing import List, Optional
import cli.interface
from tabulate import tabulate
from datetime import datetime
import os
import json
from utils.stuff import slow_type as slow
from core import task_database


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



class Role:
    def __init__(self, name: str, commitments: Optional[List[Commitment]] = None): 
        self.name = name
        self.commitments = commitments if commitments else []

    def __repr__(self):
        return(f"Role(name='{self.name}', commitments={self.commitments})")
    
