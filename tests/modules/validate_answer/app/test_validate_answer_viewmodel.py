from src.modules.validate_answer.app.validate_answer_viewmodel import ValidateAnswerViewmodel
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


class Test_ValidateAnswerViewmodel:
    def test_validate_answer_viewmodel(self):
        repo = AnswerRepositoryMock()
        answer = repo.all_answers[0]
        viewmodel = ValidateAnswerViewmodel(answer).to_dict()
        
        assert viewmodel == {
            "answer": {
                "answer_id": "0",
                "exercise_id": "111-111-111",
                "content": "A resposta vem aqui!",
                "email": "22.01049-0@maua.br",
                "is_right": 0,
            },
            "message": "Answer validated successfully"
        }