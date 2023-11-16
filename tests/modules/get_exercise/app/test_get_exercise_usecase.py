import pytest
from src.modules.get_exercise.app.get_exercise_usecase import GetExerciseUsecase
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock
from fastapi import HTTPException

class Test_GetExerciseUsecase:
    def test_get_exercise_usecase(self):
        repo = ExerciseRepositoryMock()
        usecase = GetExerciseUsecase(repo)
        exercise = usecase(repo.get_all_exercises()[0].exercise_id)
        assert exercise == repo.get_all_exercises()[0]
        
    def test_get_exercise_usecase_not_found(self):
        repo = ExerciseRepositoryMock()
        usecase = GetExerciseUsecase(repo)
        
        with pytest.raises(HTTPException) as exc:
            usecase("not_found")
        assert exc.value.status_code == 404
        assert exc.value.detail == "Exercise not found"