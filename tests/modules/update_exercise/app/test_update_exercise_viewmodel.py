from src.modules.update_exercise.app.update_exercise_viewmodel import UpdateExerciseViewmodel
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


class Test_UpdateExerciseViewmodel:
    def test_update_exercise_viewmodel(self):
        repo = ExerciseRepositoryMock()
        exercise = repo.update_exercise_by_id(repo.get_all_exercises()[0].exercise_id, new_title="Quem inventou o Linux?")
        viewmodel = UpdateExerciseViewmodel(exercise)
        expected = {'exercise': {'exercise_id': '111-111-111', 'title': 'Quem inventou o Linux?', 'enunciado': 'Quem foi o primeiro presidente do Brasil?', 'creation_date': 1673319600000, 'expiration_date': 1676084400000, 'correct_answer': 'Marechal Deodoro'}, 'message': 'Exercise updated successfully'}
        
        assert viewmodel.to_dict() == expected