from src.shared.domain.entities.exercise import Exercise
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


class Test_ExerciseRepositoryMock:
    def test_create_exercise(self):
        repo = ExerciseRepositoryMock()
        new_exercise = repo.create_exercise(exercise=Exercise(exercise_id="111-333-111", title="Teste", enunciado="Teste", creation_date=1699011271291, expiration_date=1699211271291, correct_answer="Teste"))
        
        assert new_exercise == repo._exercises[-1]

    def test_get_exercise_by_id(self):
        repo = ExerciseRepositoryMock()
        exercise_id = repo._exercises[0].exercise_id
        exercise = repo.get_exercise_by_id(exercise_id=exercise_id)

        assert exercise == repo._exercises[0]

    def test_update_exercise_by_id(self):
        repo = ExerciseRepositoryMock()
        exercise_id = repo._exercises[0].exercise_id
        new_exercise = repo.update_exercise_by_id(exercise_id=exercise_id, new_title="Atualizado", new_enunciado="Anunciado Atualizado", new_creation_date=1699011271291, new_expiration_date=1699211271291, new_correct_answer="Answer Teste")

        assert repo._exercises[0] == new_exercise

    def test_delete_exercise_by_id(self):
        repo = ExerciseRepositoryMock()
        len_before = len(repo._exercises)
        exercise_id = repo._exercises[0].exercise_id
        exercise = repo.delete_exercise_by_id(exercise_id=exercise_id)

        assert exercise not in repo._exercises
        assert len(repo._exercises) == len_before - 1
        
    def test_get_all_exercises(self):
        repo = ExerciseRepositoryMock()
        exercises = repo.get_all_exercises()
        assert exercises == repo._exercises