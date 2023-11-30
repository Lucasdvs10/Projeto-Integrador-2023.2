from fastapi.exceptions import HTTPException
import pytest
from src.modules.get_answer.app.get_answer_controller import GetAnswerController
from src.modules.get_answer.app.get_answer_usecase import GetAnswerUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


class Test_GetAnswerController:
    def test_get_answer_controller(self):
        repo = AnswerRepositoryMock()
        usecase = GetAnswerUsecase(repo)
        controller = GetAnswerController(usecase)
        request = HttpRequest(body={
            "answer_id": repo.all_answers[0].answer_id
        })
        response = controller(request)
        
        expected = {'answer': {"answer_id": "0", "exercise_id":"111-111-111", "email":"22.01049-0@maua.br", "content":"A resposta vem aqui!", "is_right":0}, 'message': 'Answer retrieved successfully'}
        
        assert response.status_code == 200
        assert response.body == expected
        
    def test_get_answer_controller_missing_answer_id(self):
        repo = AnswerRepositoryMock()
        usecase = GetAnswerUsecase(repo)
        controller = GetAnswerController(usecase)
        request = HttpRequest(body={})
        
        with pytest.raises(HTTPException) as exc:
            response = controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Missing answer id"
        
    def test_get_answer_controller_wrong_answer_id_type(self):
        repo = AnswerRepositoryMock()
        usecase = GetAnswerUsecase(repo)
        controller = GetAnswerController(usecase)
        request = HttpRequest(body={
            "answer_id": 123
        })
        
        with pytest.raises(HTTPException) as exc:
            response = controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Answer id must be a string"