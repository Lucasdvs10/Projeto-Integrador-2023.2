from src.modules.update_exercise.app.update_exercise_presenter import update_exercise_presenter
from src.modules.update_exercise.app.update_exercise_usecase import UpdateExerciseUsecase
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


class Test_UpdateExercisePresenter:
    def test_update_exercise_presenter(self):
        event = {
            'body' : {
                "exercise_id": "111-111-111",
                "new_title": "New title",
                "new_enunciado": "New enunciado",
                "new_creation_date": 1577847600000,
                "new_expiration_date": 3387133800000,
            }
        }
        
        response = update_exercise_presenter(event, None)
        
        assert response["status_code"] == 200
        assert response["body"] == {'exercise': {'exercise_id': '111-111-111', 'title': 'New title', 'enunciado': 'New enunciado', 'creation_date': 1577847600000, 'expiration_date': 3387133800000, 'correct_answer': 'Marechal Deodoro'}, 'message': 'Exercise updated successfully'}