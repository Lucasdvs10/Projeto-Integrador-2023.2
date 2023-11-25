from src.shared.domain.repositories.answer_repository_interface import IAnswerRepository
from fastapi import HTTPException, status

class GetAnswerUsecase:
    def __init__(self, repo: IAnswerRepository):
        self.repo = repo
        
    def __call__(self, answer_id: str):
        answer = self.repo.get_answer(answer_id)
        if answer is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Answer not found")
        
        return answer