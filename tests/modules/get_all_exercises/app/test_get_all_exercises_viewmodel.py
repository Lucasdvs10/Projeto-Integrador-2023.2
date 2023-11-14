from src.modules.get_all_exercises.app.get_all_exercises_viewmodel import GetAllExercisesViewmodel
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


class Test_GetAllExercisesViewmodel:
    def test_get_all_exercises_viewmodel(self):
        repo = ExerciseRepositoryMock()
        exercises = repo.get_all_exercises()
        viewmodel = GetAllExercisesViewmodel(exercises).to_dict()
        
        expected = {'exercises': [{'exercise_id': '111-111-111', 'title': 'Primeiro Presidente do Brasil', 'enunciado': 'Quem foi o primeiro presidente do Brasil?', 'creation_date': 1673319600000, 'expiration_date': 1676084400000, 'correct_answer': 'Marechal Deodoro'}, {'exercise_id': '111-222-111', 'title': 'Qual lingua é mais antiga', 'enunciado': 'Qual lingua é mais antiga: Python ou java', 'creation_date': 1673319600000, 'expiration_date': 1676084400000, 'correct_answer': 'Python'}], 'message': 'Exercises retrieved successfully'}
        
        assert viewmodel == expected