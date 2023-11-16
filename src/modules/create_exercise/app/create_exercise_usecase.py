from src.shared.domain.entities.exercise import Exercise
from src.shared.domain.repositories.exercise_repository_interface import IExerciseRepository
from fastapi import HTTPException, status

class CreateExerciseUseCase:
    def __init__(self, repo: IExerciseRepository):
        self.repo = repo
        
    def __call__(self, exercise_id: str, title: str, enunciado: str, creation_date: int, expiration_date: int, correct_answer: str):
        if self.repo.get_exercise_by_id(exercise_id) is not None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Exercise already exists")
        
        exercise = Exercise(exercise_id, title, enunciado, creation_date, expiration_date, correct_answer)
        
        return self.repo.create_exercise(exercise)