from src.shared.domain.repositories.exercise_repository_interface import IExerciseRepository
from fastapi import HTTPException, status

class DeleteExerciseUsecase:
    def __init__(self, repo: IExerciseRepository):
        self.repo = repo
        
    def __call__(self, exercise_id: str):
        exercise = self.repo.delete_exercise_by_id(exercise_id)
        if not exercise:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exercise not found")
        return exercise