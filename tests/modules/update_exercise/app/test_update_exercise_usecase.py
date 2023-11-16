import copy
from src.modules.update_exercise.app.update_exercise_usecase import UpdateExerciseUsecase
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock
from fastapi import HTTPException
import pytest

class Test_UpdateExerciseUsecase:
    def test_update_exercise_usecase(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        old_exercise = copy.deepcopy(repo.get_exercise_by_id(exercise_id))        

        updated_exercise = usecase(exercise_id, new_title="Quem inventou o Linux?", new_enunciado="Quem inventou o Linux?", new_creation_date=1673319600000, new_expiration_date=1676084400000, new_correct_answer="Linus Torvalds")
        
        assert old_exercise != updated_exercise
        assert repo.get_exercise_by_id(exercise_id) == updated_exercise
        
    def test_update_exercise_usecase_with_nonexistent_exercise(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        exercise_id = "notfound"
        
        with pytest.raises(HTTPException) as exc:
            usecase(exercise_id, new_title="Quem inventou o Linux?", new_enunciado="Quem inventou o Linux?", new_creation_date=1673319600000, new_expiration_date=1676084400000, new_correct_answer="Linus Torvalds")
        assert exc.value.status_code == 404
        assert exc.value.detail == "Exercise not found"