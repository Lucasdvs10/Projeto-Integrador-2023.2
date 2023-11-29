from src.shared.domain.entities.answer import Answer
from src.shared.domain.repositories.answer_repository_interface import IAnswerRepository
from fastapi import HTTPException, status

class CreateAnswerUsecase:
    def __init__(self, repo: IAnswerRepository):
        self.repo = repo
        
    def __call__(self, answer_id, exercise_id: str, email: str, content: str, is_right: int):        
        if self.repo.get_answer(answer_id):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Answer already exists")
        answer = Answer(answer_id, exercise_id, email, content, is_right)
        return self.repo.create_answer(answer)