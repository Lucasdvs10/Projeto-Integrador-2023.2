from fastapi import HTTPException
import pytest
from src.modules.get_all_exercises.app.get_all_exercises_usecase import GetAllExercisesUsecase
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


class Test_GetAllExercisesUsecase:
    def test_get_all_exercises_usecase(self):
        repo = ExerciseRepositoryMock()
        usecase = GetAllExercisesUsecase(repo)
        exercises = usecase()
        assert exercises == repo._exercises
        
    def test_get_all_exercises_usecase_404(self):
        repo = ExerciseRepositoryMock()
        usecase = GetAllExercisesUsecase(repo)
        repo._exercises = []
        with pytest.raises(HTTPException) as exc:
            exercises = usecase()