from src.shared.domain.repositories.answer_repository_interface import IAnswerRepository
from fastapi import HTTPException, status

class GetAnswersUsecase:
    def __init__(self, repo: IAnswerRepository):
        self.repo = repo
        
    def __call__(self, exercise_id: str):
        answers = self.repo.get_answers(exercise_id=exercise_id)
        if answers is None or len(answers) == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Answers not found")
        
        return answers