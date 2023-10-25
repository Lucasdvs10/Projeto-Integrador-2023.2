import abc
from typing import Optional
from src.shared.domain.entities.user import User

class IUserRepository:
    
    @abc.abstractmethod
    def create_user(self, user: User):
        pass
    
    @abc.abstractmethod
    def update_user_by_email(self, email: str, new_name: Optional[str], new_role: Optional[str], new_password: Optional[str], new_disciplines: Optional[list], new_exercises_solved: Optional[list]):
        pass
    
    @abc.abstractmethod
    def get_user_by_email(self, email: str):
        pass
    
    @abc.abstractmethod
    def delete_user_by_email(self, email: str):
        pass