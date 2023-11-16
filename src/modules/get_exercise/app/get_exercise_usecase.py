from src.shared.domain.repositories.exercise_repository_interface import IExerciseRepository
from fastapi import HTTPException, status

class GetExerciseUsecase:
    def __init__(self, repo: IExerciseRepository):
        self.repo = repo
        
    def __call__(self, exercise_id: str):
        exercise = self.repo.get_exercise_by_id(exercise_id)
        if exercise is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exercise not found")
        
        return exercise