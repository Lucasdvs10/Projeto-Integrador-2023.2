import dataclasses
import re
from typing import List

from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityParameterTypeError

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
            raise EntityParameterTypeError("email")
        self._email = email
        
        if type(name) != str:
            raise EntityParameterTypeError("name")
        if not self.NAME_MIN_LENGTH <= len(name) <= self.NAME_MAX_LENGTH:
            raise ValueError(f"Name must be between {self.NAME_MIN_LENGTH} and {self.NAME_MAX_LENGTH} characters long")
        self._name = name
        
        if type(role) != ROLE:
            raise EntityParameterTypeError("role")
        if role not in ROLE:
            raise ValueError(f"Role must be one of {ROLE}")
        self._role = role

        if type(password) != str:
            raise EntityParameterTypeError("password")
        if not self.PASSWORD_MIN_LENGTH <= len(password) <= self.PASSWORD_MAX_LENGTH:
            raise ValueError(f"Password must be between {self.PASSWORD_MIN_LENGTH} and {self.PASSWORD_MAX_LENGTH} characters long")
        self._password = password
        
        if type(exercises_solved) != list:
            raise EntityParameterTypeError("exercises_solved")
        # if not all(Exercise.validate_id(exercise_id) for exercise_id in exercises_solved):
        #     raise ValueError("Invalid exercise id")
        self._exercises_solved = exercises_solved
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not self.validate_email(value):
            raise EntityParameterTypeError("email")
        self._email = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) != str:
            raise EntityParameterTypeError("name")
        if not self.NAME_MIN_LENGTH <= len(value) <= self.NAME_MAX_LENGTH:
            raise ValueError(f"Name must be between {self.NAME_MIN_LENGTH} and {self.NAME_MAX_LENGTH} characters long")
        self._name = value
        
    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, value):
        if type(value) != ROLE:
            raise EntityParameterTypeError("role")
        if value not in ROLE:
            raise ValueError(f"Role must be one of {ROLE}")
        self._role = value
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        if type(value) != str:
            raise EntityParameterTypeError("password")
        if not self.PASSWORD_MIN_LENGTH <= len(value) <= self.PASSWORD_MAX_LENGTH:
            raise ValueError(f"Password must be between {self.PASSWORD_MIN_LENGTH} and {self.PASSWORD_MAX_LENGTH} characters long")
        self._password = value
        
    @property
    def exercises_solved(self):
        return self._exercises_solved
    
    @exercises_solved.setter
    def exercises_solved(self, value):
        if type(value) != list:
            raise EntityParameterTypeError("exercises_solved")
        # if not all(Exercise.validate_id(exercise_id) for exercise_id in value):
        #     raise ValueError("Invalid exercise id")
        self._exercises_solved = value
     
    def validate_email(self, email):
        if type(email) != str:
            return False
        regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        return bool(re.fullmatch(regex, email))