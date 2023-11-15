from typing import List
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from fastapi import HTTPException, status

class BatchCreateUsersUsecase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo
        
    def __call__(self, users: List[User]):
        emails = []
        for user in users:
            if self.repo.get_user_by_email(user.email) is not None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with e-mail {user.email} already exists")
            if user.email in emails:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Duplicate e-mail {user.email}")
            emails.append(user.email)
            
        return self.repo.batch_create_users(users)