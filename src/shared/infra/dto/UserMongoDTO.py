from typing import List

from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE


class UserMongoDTO:
    email: str
    name: str
    role: ROLE
    password: str
    exercises_solved: List[str]
    
    def __init__(self, email, name, role, password, exercises_solved):
        self.email = email
        self.name = name
        self.role = role
        self.password = password
        self.exercises_solved = exercises_solved
        
    @staticmethod
    def from_entity(user: User) -> 'UserMongoDTO':
        return UserMongoDTO(user.email, user.name, user.role, user.password, user.exercises_solved)
    
    def to_mongo(self) -> dict:
        return {
            'email': self.email,
            'name': self.name,
            'role': self.role.value,
            'password': self.password,
            'exercises_solved': self.exercises_solved
        }
    
    @staticmethod
    def from_mongo(user: dict) -> 'UserMongoDTO':
        return UserMongoDTO(user['email'], user['name'], ROLE(user['role']), user['password'], user['exercises_solved'])
    
    def to_entity(self) -> User:
        return User(self.email, self.name, self.role, self.password, self.exercises_solved)
    
    def __repr__(self):
        return f"UserMongoDTO(email={self.email}, name={self.name}, role={self.role.value}, password={self.password}, exercises_solved={self.exercises_solved})"
    
    def __eq__(self, other):
        if not isinstance(other, UserMongoDTO):
            return False
        return self.email == other.email and self.name == other.name and self.role == other.role and self.password == other.password and self.exercises_solved == other.exercises_solved