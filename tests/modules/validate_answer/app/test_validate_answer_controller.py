from src.modules.validate_answer.app.validate_answer_controller import ValidateAnswerController
from src.modules.validate_answer.app.validate_answer_usecase import ValidateAnswerUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock
import pytest
from fastapi import HTTPException

from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

class Test_ValidateAnswerController:
    def test_validate_answer_controller(self):
        answer_repo = AnswerRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ValidateAnswerUsecase(answer_repo, user_repo)
        controller = ValidateAnswerController(usecase)
        
        request = HttpRequest(body={
            "answer_id": answer_repo.all_answers[0].answer_id,
            "is_right": 1
        })
        
        response = controller(request)
        
        assert response.status_code == 200
        assert response.body.answer.answer_id == answer_repo.all_answers[0].answer_id
        assert response.body.answer.is_right == 1
    
    def test_validate_answer_controller_missing_answer_id(self):
        answer_repo = AnswerRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ValidateAnswerUsecase(answer_repo, user_repo)
        controller = ValidateAnswerController(usecase)
        
        request = HttpRequest(body={
            "is_right": 1
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Missing answer_id"
    
    def test_validate_answer_controller_invalid_answer_id(self):
        answer_repo = AnswerRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ValidateAnswerUsecase(answer_repo, user_repo)
        controller = ValidateAnswerController(usecase)
        
        request = HttpRequest(body={
            "answer_id": 1,
            "is_right": 1
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid answer_id"
    
    def test_validate_answer_controller_missing_is_right(self):
        answer_repo = AnswerRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ValidateAnswerUsecase(answer_repo, user_repo)
        controller = ValidateAnswerController(usecase)
        
        request = HttpRequest(body={
            "answer_id": answer_repo.all_answers[0].answer_id
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Missing is_right"
    
    def test_validate_answer_controller_invalid_is_right(self):
        answer_repo = AnswerRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ValidateAnswerUsecase(answer_repo, user_repo)
        controller = ValidateAnswerController(usecase)
        
        request = HttpRequest(body={
            "answer_id": answer_repo.all_answers[0].answer_id,
            "is_right": 2
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid is_right"