import pytest
from src.shared.domain.entities.exercise import Exercise
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock
from src.shared.infra.repositories.exercise_repository_mongo import ExerciseRepositoryMongo


class Test_ExerciseRepositoryMongo:
    
    @pytest.mark.skip(reason="Not implemented yet")
    def test_batch_create_exercises(self):
        repo = ExerciseRepositoryMongo()
        mock = ExerciseRepositoryMock()
        exercises = mock.get_all_exercises()
        resp = repo.batch_create_exercises(exercises)
        
        assert resp == exercises
        
    @pytest.mark.skip(reason="Not implemented yet")
    def test_get_all_exercises():
        repo = ExerciseRepositoryMongo()
        resp = repo.get_all_exercises()

        assert resp is not None
    
    @pytest.mark.skip(reason="Not implemented yet")
    def test_create_exercise(self):
        repo = ExerciseRepositoryMongo()
        new_exercise = Exercise("test_id", "test_title", "test_enunciado", 1620000000000, 1620050000000, "test_correct_answer")
        len_before = len(repo.get_all_exercises())
        resp = repo.create_exercise(new_exercise)
        
        assert resp == new_exercise
        assert len(repo.get_all_exercises()) == len_before + 1
        
    @pytest.mark.skip(reason="Not implemented yet")
    def test_get_exercise_by_id(self):
        repo = ExerciseRepositoryMongo()
        resp = repo.get_exercise_by_id("test_id")
        
        assert resp is not None
        
    @pytest.mark.skip(reason="Not implemented yet")
    def test_update_exercise_by_id(self):
        repo = ExerciseRepositoryMongo()
        resp = repo.update_exercise_by_id("test_id", new_title="new_test_title")
        
        assert resp.title == "new_test_title"
        assert repo.get_exercise_by_id("test_id").title == "new_test_title"
        
    @pytest.mark.skip(reason="Not implemented yet")
    def test_delete_exercise_by_id(self):
        repo = ExerciseRepositoryMongo()
        len_before = len(repo.get_all_exercises())
        resp = repo.delete_exercise_by_id("test_id")
        
        assert resp is not None
        assert len(repo.get_all_exercises()) == len_before - 1