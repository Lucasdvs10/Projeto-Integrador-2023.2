from typing import Optional
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from fastapi import HTTPException, status

class UpdateUserUsecase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo
        
    def __call__(self, email: str, new_name: Optional[str] = None, new_role: Optional[str] = None, new_password: Optional[str] = None, new_exercises_solved: Optional[list] = None):
        
        if self.repo.get_user_by_email(email) is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        return self.repo.update_user_by_email(email, new_name, new_role, new_password, new_exercises_solved)