from fastapi.exceptions import HTTPException
import pytest
from src.modules.update_answer.app.update_answer_controller import UpdateAnswerController
from src.modules.update_answer.app.update_answer_usecase import UpdateAnswerUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock
from fastapi.exceptions import HTTPException
import pytest
from src.modules.update_answer.app.update_answer_controller import UpdateAnswerController
from src.modules.update_answer.app.update_answer_usecase import UpdateAnswerUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


class Test_UpdateAnswerController:
    def test_update_answer_controller(self):
        repo = AnswerRepositoryMock()
        usecase = UpdateAnswerUsecase(repo)
        controller = UpdateAnswerController(usecase)
        answer_id = repo.all_answers[0].answer_id
        httpRequest = HttpRequest(body={
            "answer_id": answer_id,
            "new_content": "New content",
            "new_email": "New email",
            "new_is_right": 1,
        })
        
        response = controller(httpRequest)
        
        assert response.status_code == 200
        assert response.body == {'answer': {"answer_id": "0", "exercise_id":"111-111-111", "email":"New email", "content":"New content", "is_right":1}, 'message': 'Answer updated successfully'}
        
    def test_update_answer_controller_missing_answer_id(self):
        repo = AnswerRepositoryMock()
        usecase = UpdateAnswerUsecase(repo)
        controller = UpdateAnswerController(usecase)
        httpRequest = HttpRequest(body={
            "new_title": "New title",
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "Answer id not provided"
        
    def test_update_answer_controller_invalid_answer_id(self):
        repo = AnswerRepositoryMock()
        usecase = UpdateAnswerUsecase(repo)
        controller = UpdateAnswerController(usecase)
        httpRequest = HttpRequest(body={
            "answer_id": 1,
            "new_title": "New title",
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "Answer id must be a string"
        
    def test_update_answer_controller_none_new_content(self):
        repo = AnswerRepositoryMock()
        usecase = UpdateAnswerUsecase(repo)
        controller = UpdateAnswerController(usecase)
        answer_id = repo.all_answers[0].answer_id
        httpRequest = HttpRequest(body={
            "answer_id": answer_id,
            "new_content": None,
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "New content can't be None"
        
    def test_update_answer_controller_invalid_new_content_type(self):
        repo = AnswerRepositoryMock()
        usecase = UpdateAnswerUsecase(repo)
        controller = UpdateAnswerController(usecase)
        answer_id = repo.all_answers[0].answer_id
        httpRequest = HttpRequest(body={
            "answer_id": answer_id,
            "new_content": 1,
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "New content must be a string"
        
    def test_update_answer_controller_invalid_new_content_length(self):
        repo = AnswerRepositoryMock()
        usecase = UpdateAnswerUsecase(repo)
        controller = UpdateAnswerController(usecase)
        answer_id = repo.all_answers[0].answer_id
        httpRequest = HttpRequest(body={
            "answer_id": answer_id,
            "new_content": "a",
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == f"New content must be between 3 and 300 characters"
      
    def test_update_answer_controller_none_new_email(self):
        repo = AnswerRepositoryMock()
        usecase = UpdateAnswerUsecase(repo)
        controller = UpdateAnswerController(usecase)
        answer_id = repo.all_answers[0].answer_id
        httpRequest = HttpRequest(body={
            "answer_id": answer_id,
            "new_content": "New content",
            "new_email": None,
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "New email can't be None"
        
    def test_update_answer_controller_invalid_new_email_type(self):
        repo = AnswerRepositoryMock()
        usecase = UpdateAnswerUsecase(repo)
        controller = UpdateAnswerController(usecase)
        answer_id = repo.all_answers[0].answer_id
        httpRequest = HttpRequest(body={
            "answer_id": answer_id,
            "new_content": "New content",
            "new_email": 1,
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "New email must be a string"
        
    def test_update_answer_controller_none_new_is_right(self):
        repo = AnswerRepositoryMock()
        usecase = UpdateAnswerUsecase(repo)
        controller = UpdateAnswerController(usecase)
        answer_id = repo.all_answers[0].answer_id
        httpRequest = HttpRequest(body={
            "answer_id": answer_id,
            "new_content": "New content",
            "new_email": "digao@gmail.com",
            "new_is_right": None,
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "New is right can't be None"
        
    def test_update_answer_controller_invalid_new_is_right_type(self):
        repo = AnswerRepositoryMock()
        usecase = UpdateAnswerUsecase(repo)
        controller = UpdateAnswerController(usecase)
        answer_id = repo.all_answers[0].answer_id
        httpRequest = HttpRequest(body={
            "answer_id": answer_id,
            "new_content": "New content",
            "new_email": "digao@gmail.com",
            "new_is_right": "invalid_is_right",
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "New is right must be an integer"