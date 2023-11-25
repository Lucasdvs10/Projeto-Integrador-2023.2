from src.modules.update_answer.app import update_answer_presenter
from src.modules.update_answer.app.update_answer_presenter import update_answer_presenter
from src.modules.update_exercise.app.update_exercise_usecase import UpdateExerciseUsecase
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


class Test_UpdateAnswerPresenter:
    def test_update_answer_presenter(self):
        event = {
            'body' : {
                "answer_id": "0",
                "new_email": "New email",
                "new_content": "New content",
                "new_is_right": 1,
            }
        }
        
        response = update_answer_presenter(event, None)
        
        assert response["status_code"] == 200
        assert response["body"] == {'answer': {"answer_id": "0", "exercise_id":"111-111-111", "email":"New email", "content":"New content", "is_right":1}, 'message': 'Answer updated successfully'}