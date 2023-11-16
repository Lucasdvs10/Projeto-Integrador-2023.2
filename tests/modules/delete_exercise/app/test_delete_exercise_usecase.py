from fastapi.exceptions import HTTPException
import pytest
from src.modules.delete_exercise.app.delete_exercise_usecase import DeleteExerciseUsecase
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


class Test_DeleteExerciseUsecase:
    def test_delete_exercise_usecase(self):
        repo = ExerciseRepositoryMock()
        usecase = DeleteExerciseUsecase(repo)
        len_before = len(repo.get_all_exercises())
        exercise_id = repo.get_all_exercises()[0].exercise_id
        exercise = usecase(exercise_id)
        assert exercise.exercise_id == exercise_id
        assert repo.get_all_exercises()[0] != exercise
        assert len(repo.get_all_exercises()) == len_before - 1
        
    def test_delete_exercise_usecase_not_found(self):
        repo = ExerciseRepositoryMock()
        usecase = DeleteExerciseUsecase(repo)
        exercise_id = "not_found"
        
        with pytest.raises(HTTPException) as exc:
            usecase(exercise_id)
        assert exc.value.status_code == 404
        assert exc.value.detail == "Exercise not found"