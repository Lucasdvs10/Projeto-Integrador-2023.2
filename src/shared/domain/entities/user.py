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
        
        if not self.validate_name(name):
            raise EntityParameterTypeError("name")
        self._name = name
        
        if not self.validate_role(role):
            raise EntityParameterTypeError("role")
        self._role = role

        if not self.validate_password(password):
            raise EntityParameterTypeError("password")
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