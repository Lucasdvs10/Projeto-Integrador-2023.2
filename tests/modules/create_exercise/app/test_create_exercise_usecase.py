from fastapi.exceptions import HTTPException
import pytest
from src.modules.create_exercise.app.create_exercise_usecase import CreateExerciseUseCase
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


class Test_CreateExerciseUseCase:
    def test_create_exercise_usecase(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        len_before = len(repo.get_all_exercises())
        new_exercise = usecase(exercise_id="1", title="title", enunciado="enunciado", creation_date=1577847600000, expiration_date=3387133800000, correct_answer="correct_answer")
        
        assert len(repo.get_all_exercises()) == len_before + 1
        assert repo.get_all_exercises()[-1] == new_exercise\
            
    def test_create_exercise_usecase_already_exists(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        with pytest.raises(HTTPException) as exc:
            usecase(exercise_id=exercise_id, title="title", enunciado="enunciado", creation_date=1577847600000, expiration_date=3387133800000, correct_answer="correct_answer")
        assert exc.value.status_code == 409
        assert exc.value.detail == "Exercise already exists"