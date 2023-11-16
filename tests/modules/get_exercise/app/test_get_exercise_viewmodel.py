from src.modules.get_exercise.app.get_exercise_viewmodel import GetExerciseViewmodel
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


class Test_GetExerciseViewmodel:
    def test_get_exercise_viewmodel(self):
        repo = ExerciseRepositoryMock()
        exercise = repo.get_exercise_by_id(repo.get_all_exercises()[0].exercise_id)
        viewmodel = GetExerciseViewmodel(exercise)
        expected = {'exercise': {'exercise_id': '111-111-111', 'title': 'Primeiro Presidente do Brasil', 'enunciado': 'Quem foi o primeiro presidente do Brasil?', 'creation_date': 1673319600000, 'expiration_date': 1676084400000, 'correct_answer': 'Marechal Deodoro'}, 'message': 'Exercise retrieved successfully'}
        
        assert viewmodel.to_dict() == expected