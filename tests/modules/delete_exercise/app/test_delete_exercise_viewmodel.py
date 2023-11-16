from src.modules.delete_exercise.app.delete_exercise_usecase import DeleteExerciseUsecase
from src.modules.delete_exercise.app.delete_exercise_viewmodel import DeleteExerciseViewmodel
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


class Test_DeleteExerciseViewmodel:
    def test_delete_exercise_viewmodel(self):
        repo = ExerciseRepositoryMock()
        usecase = DeleteExerciseUsecase(repo)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        new_exercise = usecase(exercise_id=exercise_id)
        viewmodel = DeleteExerciseViewmodel(new_exercise).to_dict()
        expected = {'exercise': {'exercise_id': '111-111-111', 'title': 'Primeiro Presidente do Brasil', 'enunciado': 'Quem foi o primeiro presidente do Brasil?', 'creation_date': 1673319600000, 'expiration_date': 1676084400000, 'correct_answer': 'Marechal Deodoro'}, 'message': 'Exercise deleted successfully'}
        
        assert viewmodel == expected