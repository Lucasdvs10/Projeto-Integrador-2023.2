import names
import dataclasses
import re
from typing import List
import random
from enum import Enum

class ROLE(Enum):
    ADMIN = "ADMIN"
    TEACHER = "TEACHER"
    STUDENT = "STUDENT"
    MONITOR = "MONITOR"
    
@dataclasses.dataclass
class User:
    _email: str
    _name: str
    _role: ROLE
    _password: str
    _exercises_solved : List[str] # List of exercise ids
    NAME_MIN_LENGTH = 3
    NAME_MAX_LENGTH = 255
    PASSWORD_MIN_LENGTH = 8
    PASSWORD_MAX_LENGTH = 255
    
    def __init__(self, email, name, role, password, exercises_solved):
        if not self.validate_email(email):
            raise Exception("email")
        self._email = email
        
        if not self.validate_name(name):
            raise Exception("name")
        self._name = name
        
        if not self.validate_role(role):
            raise Exception("role")
        self._role = role

        if not self.validate_password(password):
            raise Exception("password")
        self._password = password
        
        if type(exercises_solved) != list:
            raise Exception("exercises_solved")
        # if not all(Exercise.validate_id(exercise_id) for exercise_id in exercises_solved):
        #     raise ValueError("Invalid exercise id")
        self._exercises_solved = exercises_solved
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not self.validate_email(value):
            raise Exception("email")
        self._email = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) != str:
            raise Exception("name")
        if not self.NAME_MIN_LENGTH <= len(value) <= self.NAME_MAX_LENGTH:
            raise ValueError(f"Name must be between {self.NAME_MIN_LENGTH} and {self.NAME_MAX_LENGTH} characters long")
        self._name = value
        
    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, value):
        if type(value) != ROLE:
            raise Exception("role")
        if value not in ROLE:
            raise ValueError(f"Role must be one of {ROLE}")
        self._role = value
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        if type(value) != str:
            raise Exception("password")
        if not self.PASSWORD_MIN_LENGTH <= len(value) <= self.PASSWORD_MAX_LENGTH:
            raise ValueError(f"Password must be between {self.PASSWORD_MIN_LENGTH} and {self.PASSWORD_MAX_LENGTH} characters long")
        self._password = value
        
    @property
    def exercises_solved(self):
        return self._exercises_solved
    
    @exercises_solved.setter
    def exercises_solved(self, value):
        if type(value) != list:
            raise Exception("exercises_solved")
        # if not all(Exercise.validate_id(exercise_id) for exercise_id in value):
        #     raise ValueError("Invalid exercise id")
        self._exercises_solved = value
     
    @staticmethod
    def validate_email(email):
        if type(email) != str:
            return False
        regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        return bool(re.fullmatch(regex, email))
    
    @staticmethod
    def validate_name(name):
        if type(name) != str:
            return False
        return User.NAME_MIN_LENGTH <= len(name) <= User.NAME_MAX_LENGTH
    
    @staticmethod
    def validate_role(role):
        if type(role) != ROLE:
            return False
        return role in ROLE
    
    @staticmethod
    def validate_password(password):
        if type(password) != str:
            return False
        return User.PASSWORD_MIN_LENGTH <= len(password) <= User.PASSWORD_MAX_LENGTH
    
    def __str__(self):
        return f"User(email={self._email}, name={self._name}, role={self._role}, password={self._password}, exercises_solved={self._exercises_solved})"

'''
_email: str
    _name: str
    _role: ROLE
    _password: str
    _exercises_solved : List[str] # will be empty []
'''

class UserGenerator:
    def generate_users(quantity: int) -> List[User]:
        ra_start = [str(i) for i in range(10, 24)]
        ra_middle = [str(i).zfill(5) for i in range(20001, 40001)]
        ra_end = [str(i) for i in range(0, 10)]
        
        user_names = [names.get_full_name() for i in range(quantity)]
        ras = [random.choice(ra_start) + "." + random.choice(ra_middle) + "-" + random.choice(ra_end) for i in range(quantity)]
        roles = [random.choice(list(ROLE)) for i in range(quantity)]
        passwords = [''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(8)) for i in range(quantity)]
        exercises_solved = [[] for i in range(quantity)]
        emails = [ras[i] + "@maua.br" for i in range(quantity)]
        
        users = [User(email=emails[i], name=user_names[i], role=roles[i], password=passwords[i], exercises_solved=exercises_solved[i]) for i in range(quantity)]
        
        return users

    def create_file(users: List[User]) -> str:
        with open('users.txt', 'w') as file:
            file.write("[")
            for user in users:
                file.write('User(' + f'email="{user.email}", name="{user.name}", role=ROLE.{user.role.value}, password="{user.password}", exercises_solved={user.exercises_solved}),\n')
            file.write("]")
        import pyperclip
        pyperclip.copy("[\n" + ",\n".join([f'User(' + f'email="{user.email}", name="{user.name}", role=ROLE.{user.role.value}, password="{user.password}", exercises_solved={user.exercises_solved})' for user in users]) + "\n]")
        return "[\n" + ",\n".join([f'User(' + f'email="{user.email}", name="{user.name}", role=ROLE.{user.role.value}, password="{user.password}", exercises_solved={user.exercises_solved})' for user in users]) + "\n]"
    
    def generate_name() -> str:
        return names.get_full_name()
    
    def generate_email() -> str:
        ra_start = random.randint(10, 23)
        ra_middle = random.randint(20001, 39999)
        ra_end = random.randint(0, 9)
        
        return f"{ra_start}.{ra_middle}-{ra_end}"
    
    def generate_password() -> str:
        return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(8))
    
    def generate_user() -> User:
        return User(email=UserGenerator.generate_email(), name=UserGenerator.generate_name(), role=UserGenerator.generate_role(), password=UserGenerator.generate_password(), exercises_solved=[])
    
    def generate_role() -> ROLE:
        return random.choice(list(ROLE))

if __name__ == "__main__":
    users = UserGenerator.generate_users(50)
    UserGenerator.create_file(users)