from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.domain.entities.user import User
from typing import Optional

class UserRepositoryMock(IUserRepository):
    def __init__(self):
        self._users = [
            User(email="22.01102-0@maua.br", name="Luigi Trevisan", role=ROLE.MONITOR, password="ebdf496f67651cddf6aaa1f0b130f1b99ce9e2e93dc2503d926edcff15aee668", exercises_solved=[]),
            User(email="22.01049-0@maua.br", name="Vitor Negresiolo", role=ROLE.STUDENT, password="ebdf496f67651cddf6aaa1f0b130f1b99ce9e2e93dc2503d926edcff15aee668", exercises_solved=[1, 2, 3]),
            User(email="22.00680-0@maua.br", name="Rodrigo Siqueira", role=ROLE.STUDENT, password="ebdf496f67651cddf6aaa1f0b130f1b99ce9e2e93dc2503d926edcff15aee668", exercises_solved=[1, 2])
        ]
    
    def create_user(self, user: User):
        self._users.append(user)
        return user
    
    def update_user_by_email(self, email: str, new_name: Optional[str] = None, new_role: Optional[str] = None, new_password: Optional[str] = None, new_exercises_solved: Optional[list] = None):
        user = self.get_user_by_email(email)
        
        if user is None:
            return None
        
        if new_name:
            user.name = new_name
        if new_role:
            user.role = new_role
        if new_password:
            user.password = new_password
        if new_exercises_solved:
            user.exercises_solved = new_exercises_solved
            
        return user
    
    def get_user_by_email(self, email: str):
        for user in self._users:
            if user.email == email:
                return user
        return None
    
    def delete_user_by_email(self, email: str):
        user = self.get_user_by_email(email)
        self._users.remove(user)
        return user
    
    def get_all_users(self):
        return self._users