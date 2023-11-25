from src.modules.update_answer.app.update_answer_viewmodel import UpdateAnswerViewmodel
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


class Test_UpdateAnswerViewmodel:
    def test_update_answer_viewmodel(self):
        repo = AnswerRepositoryMock()
        answer = repo.update_answer(repo.all_answers[0].answer_id, new_content="New content", new_email="New email", new_is_right=1)
        viewmodel = UpdateAnswerViewmodel(answer)
        expected = {'answer': {"answer_id": "0", "exercise_id":"111-111-111", "email":"New email", "content":"New content", "is_right":1}, 'message': 'Answer updated successfully'}
        
        assert viewmodel.to_dict() == expected