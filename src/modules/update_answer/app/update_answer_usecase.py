from typing import Optional
from src.shared.domain.repositories.answer_repository_interface import IAnswerRepository
from fastapi import HTTPException, status

class UpdateAnswerUsecase:
    def __init__(self, repo: IAnswerRepository):
        self.repo = repo
        
    def __call__(self, answer_id: str, new_content: Optional[str] = None, new_email: Optional[str] = None, new_is_right: Optional[int] = None):
        
        if answer_id is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Answer id not provided")
        if self.repo.get_answer(answer_id) is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Answer not found")

        return self.repo.update_answer(answer_id,  new_content, new_email, new_is_right)