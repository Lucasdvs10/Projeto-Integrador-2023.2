from src.shared.domain.repositories.user_repository_interface import IUserRepository
from fastapi import HTTPException, status

class DeleteUserUsecase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo
        
    def __call__(self, email: str):
        user = self.repo.get_user_by_email(email)
        
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        return self.repo.delete_user_by_email(email)