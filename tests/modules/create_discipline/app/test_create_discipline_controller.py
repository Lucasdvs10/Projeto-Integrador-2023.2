import pytest
from src.modules.create_discipline.app.create_discipline_controller import CreateDisciplineController
from src.modules.create_discipline.app.create_discipline_usecase import CreateDisciplineUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock
from fastapi import HTTPException

class Test_CreateDisciplineController:
    def test_create_discipline_controller(self):
        repo = DisciplineRepositoryMock()
        usecase = CreateDisciplineUsecase(repo)
        controller = CreateDisciplineController(usecase)
        
        request = HttpRequest(body={
            "name": "Discipline 1",
            "year": 1,
            "students_emails_list": ["22.01102-0@maua.br"]
        })
        response = controller(request)
        
        assert response.status_code == 201
        assert response.body["discipline"]["name"] == "Discipline 1"
        assert response.body["message"] == "Discipline created successfully"
        
    def test_create_discipline_controller_missing_name(self):
        repo = DisciplineRepositoryMock()
        usecase = CreateDisciplineUsecase(repo)
        controller = CreateDisciplineController(usecase)
        
        request = HttpRequest(body={
            "year": 1,
            "students_emails_list": []
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Missing name"
        
    def test_create_discipline_controller_invalid_name(self):
        repo = DisciplineRepositoryMock()
        usecase = CreateDisciplineUsecase(repo)
        controller = CreateDisciplineController(usecase)
        
        request = HttpRequest(body={
            "name": 1,
            "year": 1,
            "students_emails_list": []
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid name"
        
    def test_create_discipline_controller_missing_year(self):
        repo = DisciplineRepositoryMock()
        usecase = CreateDisciplineUsecase(repo)
        controller = CreateDisciplineController(usecase)
        
        request = HttpRequest(body={
            "name": "Discipline 1",
            "students_emails_list": []
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Missing year"
        
    def test_create_discipline_controller_digit_string_year(self):
        repo = DisciplineRepositoryMock()
        usecase = CreateDisciplineUsecase(repo)
        controller = CreateDisciplineController(usecase)
        
        request = HttpRequest(body={
            "name": "Discipline 1",
            "year": "1",
            "students_emails_list": []
        })
        response = controller(request)
        
        assert response.status_code == 201
        assert response.body["discipline"]["year"] == 1
        assert response.body["message"] == "Discipline created successfully"
        
    def test_create_discipline_controller_invalid_year(self):
        repo = DisciplineRepositoryMock()
        usecase = CreateDisciplineUsecase(repo)
        controller = CreateDisciplineController(usecase)
        
        request = HttpRequest(body={
            "name": "Discipline 1",
            "year": "a",
            "students_emails_list": []
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid year"
        
    def test_create_discipline_controller_missing_students_emails_list(self):
        repo = DisciplineRepositoryMock()
        usecase = CreateDisciplineUsecase(repo)
        controller = CreateDisciplineController(usecase)
        
        request = HttpRequest(body={
            "name": "Discipline 1",
            "year": 1
        })
        response = controller(request)
        
        assert response.status_code == 201
        assert response.body["discipline"]["students_emails_list"] == []
        assert response.body["message"] == "Discipline created successfully"
        
    def test_create_discipline_controller_non_list_students_emails_list(self):
        repo = DisciplineRepositoryMock()
        usecase = CreateDisciplineUsecase(repo)
        controller = CreateDisciplineController(usecase)
        
        request = HttpRequest(body={
            "name": "Discipline 1",
            "year": 1,
            "students_emails_list": "a"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid students_emails_list"
        
    def test_create_discipline_controller_invalid_email_students_emails_list(self):
        repo = DisciplineRepositoryMock()
        usecase = CreateDisciplineUsecase(repo)
        controller = CreateDisciplineController(usecase)
        
        request = HttpRequest(body={
            "name": "Discipline 1",
            "year": 1,
            "students_emails_list": ["a"]
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid email (a)"