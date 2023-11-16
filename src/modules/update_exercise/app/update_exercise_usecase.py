from typing import Optional
from src.shared.domain.repositories.exercise_repository_interface import IExerciseRepository
from fastapi import HTTPException, status

class UpdateExerciseUsecase:
    def __init__(self, repo: IExerciseRepository):
        self.repo = repo
        
    def __call__(self, exercise_id: str, new_title: Optional[str] = None, new_enunciado: Optional[str] = None, new_creation_date: Optional[int] = None, new_expiration_date: Optional[int] = None, new_correct_answer: Optional[str] = None):
        
        if self.repo.get_exercise_by_id(exercise_id) is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exercise not found")

        return self.repo.update_exercise_by_id(exercise_id, new_title, new_enunciado, new_creation_date, new_expiration_date, new_correct_answer)