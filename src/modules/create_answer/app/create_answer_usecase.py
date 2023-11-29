from src.shared.domain.entities.answer import Answer
from src.shared.domain.repositories.answer_repository_interface import IAnswerRepository
from fastapi import HTTPException, status

from src.shared.domain.repositories.exercise_repository_interface import IExerciseRepository

class CreateAnswerUsecase:
    def __init__(self, answer_repo: IAnswerRepository, exercise_repo: IExerciseRepository):
        self.answer_repo = answer_repo
        self.exercise_repo = exercise_repo
        
    def __call__(self, answer_id, exercise_id: str, email: str, content: str, is_right: int):        
        if self.repo.get_answer(answer_id):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Answer already exists")
        if not self.exercise_repo.get_exercise(exercise_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exercise not found")
        answer = Answer(answer_id, exercise_id, email, content, is_right)
        return self.repo.create_answer(answer)