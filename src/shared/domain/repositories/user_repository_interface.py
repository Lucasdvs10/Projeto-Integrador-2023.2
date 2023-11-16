import abc
from typing import Optional
from src.shared.domain.entities.user import User

class IUserRepository:
    
    @abc.abstractmethod
    def create_user(self, user: User):
        pass
    
    @abc.abstractmethod
    def update_user_by_email(self, email: str, new_name: Optional[str] = None, new_role: Optional[str] = None, new_password: Optional[str] = None, new_exercises_solved: Optional[list] = None):
        pass
    
    @abc.abstractmethod
    def get_user_by_email(self, email: str):
        pass
    
    @abc.abstractmethod
    def delete_user_by_email(self, email: str):
        pass
    
    @abc.abstractmethod
    def get_all_users(self):
        pass
    
    @abc.abstractmethod
    def batch_create_users(self, users: list):
        pass