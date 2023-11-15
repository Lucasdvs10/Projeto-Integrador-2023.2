from typing import List
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE


class UserViewmodel:
    email: str
    name: str
    role: ROLE
    exercises_solved : List[str]
    
    def __init__(self, user: User):
        self.email = user.email
        self.name = user.name
        self.role = user.role
        self.exercises_solved = user.exercises_solved
        
    def to_dict(self):
        return {
            "email": self.email,
            "name": self.name,
            "role": self.role.value,
            "exercises_solved": self.exercises_solved
        }
        
class BatchCreateUsersViewmodel:
    users: List[UserViewmodel]
    
    def __init__(self, users: List[User]):
        self.users = [UserViewmodel(user) for user in users]
        
    def to_dict(self):
        return {
            "users": [user.to_dict() for user in self.users],
            "message": "Users created successfully"
        }