from src.modules.get_answer.app.get_answer_viewmodel import GetAnswerViewmodel
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


class Test_GetAnswerViewmodel:
    def test_get_answer_viewmodel(self):
        repo = AnswerRepositoryMock()
        answer = repo.get_answer(repo.all_answers[0].answer_id)
        viewmodel = GetAnswerViewmodel(answer)
        expected = {'answer': {'answer_id': "0", "exercise_id": '111-111-111', 'content': 'A resposta vem aqui!', 'email': 'umemail@gmail.com', 'is_right': 0}, 'message': 'Answer retrieved successfully'}
        
        assert viewmodel.to_dict() == expected