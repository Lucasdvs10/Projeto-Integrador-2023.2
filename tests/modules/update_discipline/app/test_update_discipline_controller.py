import pytest
from src.modules.update_discipline.app.update_discipline_controller import UpdateDisciplineController
from src.modules.update_discipline.app.update_discipline_usecase import UpdateDisciplineUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock
from fastapi import HTTPException

class Test_UpdateDisciplineController:
    def test_update_discipline_controller(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        controller = UpdateDisciplineController(usecase)
        discipline_id = repo.all_disciplines[0].discipline_id
        request = HttpRequest(body={
            "discipline_id": discipline_id,
            "new_name": "New name",
            "new_year": 2,
            "new_students_list": ["22.01102-0@maua.br"]
        })
        
        response = controller(request)
        
        assert response.status_code == 200
        assert response.body["discipline"]["discipline_id"] == discipline_id
        assert response.body["message"] == "Discipline updated successfully"
        
    def test_update_discipline_controller_with_missing_discipline_id(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        controller = UpdateDisciplineController(usecase)
        request = HttpRequest(body={
            "new_name": "New name",
            "new_year": 2,
            "new_students_list": []
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Missing discipline_id"
        
    def test_update_discipline_controller_with_invalid_discipline_id(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        controller = UpdateDisciplineController(usecase)
        request = HttpRequest(body={
            "discipline_id": "invalid_discipline_id",
            "new_name": "New name",
            "new_year": 2,
            "new_students_list": []
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid discipline_id"
        
    def test_update_discipline_controller_with_none_new_name(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        controller = UpdateDisciplineController(usecase)
        discipline_id = repo.all_disciplines[0].discipline_id
        request = HttpRequest(body={
            "discipline_id": discipline_id,
            "new_name": None,
            "new_year": 2,
            "new_students_list": []
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Name can't be None"
        
    def test_update_discipline_controller_with_invalid_new_name(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        controller = UpdateDisciplineController(usecase)
        discipline_id = repo.all_disciplines[0].discipline_id
        request = HttpRequest(body={
            "discipline_id": discipline_id,
            "new_name": 123,
            "new_year": 2,
            "new_students_list": []
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "New name must be a string"
        
    def test_update_discipline_controller_with_none_new_year(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        controller = UpdateDisciplineController(usecase)
        discipline_id = repo.all_disciplines[0].discipline_id
        request = HttpRequest(body={
            "discipline_id": discipline_id,
            "new_name": "New name",
            "new_year": None,
            "new_students_list": []
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Year can't be None"
        
    def test_update_discipline_controller_with_digit_string_new_year(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        controller = UpdateDisciplineController(usecase)
        discipline_id = repo.all_disciplines[0].discipline_id
        request = HttpRequest(body={
            "discipline_id": discipline_id,
            "new_name": "New name",
            "new_year": "2",
            "new_students_list": []
        })
        
        response = controller(request)
        
        assert response.status_code == 200
        assert response.body["discipline"]["year"] == 2
        assert response.body["message"] == "Discipline updated successfully"
        
    def test_update_discipline_controller_with_invalid_new_year(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        controller = UpdateDisciplineController(usecase)
        discipline_id = repo.all_disciplines[0].discipline_id
        request = HttpRequest(body={
            "discipline_id": discipline_id,
            "new_name": "New name",
            "new_year": "invalid_year",
            "new_students_list": []
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "New year must be an integer"
        
    def test_update_discipline_controller_with_none_new_students_list(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        controller = UpdateDisciplineController(usecase)
        discipline_id = repo.all_disciplines[0].discipline_id
        request = HttpRequest(body={
            "discipline_id": discipline_id,
            "new_name": "New name",
            "new_year": 2,
            "new_students_list": None
        })
        
        response = controller(request)
        
        assert response.status_code == 200
        assert response.body["discipline"]["students_emails_list"] == []
        assert response.body["message"] == "Discipline updated successfully"
        
    def test_update_discipline_controller_with_empty_new_students_list(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        controller = UpdateDisciplineController(usecase)
        discipline_id = repo.all_disciplines[0].discipline_id
        request = HttpRequest(body={
            "discipline_id": discipline_id,
            "new_name": "New name",
            "new_year": 2,
            "new_students_list": []
        })
        
        response = controller(request)
        
        assert response.status_code == 200
        assert response.body["discipline"]["students_emails_list"] == []
        assert response.body["message"] == "Discipline updated successfully"
        
    def test_update_discipline_controller_with_invalid_new_students_list_type(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        controller = UpdateDisciplineController(usecase)
        request = HttpRequest(body={
            "discipline_id": repo.all_disciplines[0].discipline_id,
            "new_name": "New name",
            "new_year": 2,
            "new_students_list": 123
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "New students list must be a list"
        
    def test_update_discipline_controller_with_invalid_new_students_list_email_type(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        controller = UpdateDisciplineController(usecase)
        request = HttpRequest(body={
            "discipline_id": repo.all_disciplines[0].discipline_id,
            "new_name": "New name",
            "new_year": 2,
            "new_students_list": [123]
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == f"Invalid email ({123})"
        
    def test_update_discipline_controller_with_invalid_new_students_list_email(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        controller = UpdateDisciplineController(usecase)
        request = HttpRequest(body={
            "discipline_id": repo.all_disciplines[0].discipline_id,
            "new_name": "New name",
            "new_year": 2,
            "new_students_list": ["notanemail.com"]
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == f"Invalid email (notanemail.com)"
        
    def test_update_discipline_controller_with_email_new_students_list(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        controller = UpdateDisciplineController(usecase)
        
        discipline_id = repo.all_disciplines[0].discipline_id
        request = HttpRequest(body={
            "discipline_id": discipline_id,
            "new_name": "New name",
            "new_year": 2,
            "new_students_list": "22.01102-0@maua.br"
        })
        
        response = controller(request)
        
        assert response.status_code == 200
        assert response.body["discipline"]["students_emails_list"] == ["22.01102-0@maua.br"]
        assert response.body["message"] == "Discipline updated successfully"