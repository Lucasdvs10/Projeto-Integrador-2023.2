from fastapi import status, HTTPException
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository


class CreateUserUsecase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo
        
    def __call__(self, email: str, name: str, role: str, password: str):
        if self.repo.get_user_by_email(email):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
        
        new_user = User(email=email, name=name, role=role, password=password, exercises_solved=[])
        return self.repo.create_user(new_user)