from src.shared.domain.repositories.exercise_repository_interface import IExerciseRepository
from fastapi import HTTPException, status

class GetAllExercisesUsecase:
    def __init__(self, repo: IExerciseRepository):
        self.repo = repo
        
    def __call__(self):
        exercises = self.repo.get_all_exercises()
        if exercises is None or len(exercises) == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No exercises found")
        return exercises