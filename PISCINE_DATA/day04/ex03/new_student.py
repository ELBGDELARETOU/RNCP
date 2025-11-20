import random
import string
from dataclasses import dataclass, field

def generate_id()-> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    name: str
    surname: str
    active: bool = field(default=True)
    
    id: str = field(init=False)
    login: str = field(init=False)
    
    def __post_init__(self):
        object.__setattr__(self, "id", generate_id())
        object.__setattr__(self, "login", self.surname.lower())
    