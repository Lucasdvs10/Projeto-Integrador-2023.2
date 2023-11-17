from fastapi.exceptions import HTTPException
import pytest
from src.modules.batch_create_disciplines.app.batch_create_disciplines_controller import BatchCreateDisciplinesController
from src.modules.batch_create_disciplines.app.batch_create_disciplines_usecase import BatchCreateDisciplinesUseCase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock


class Test_BatchCreateDisciplinesController:
    def test_batch_create_disciplines_controller(self):
        repo = DisciplineRepositoryMock()
        usecase = BatchCreateDisciplinesUseCase(repo)
        controller = BatchCreateDisciplinesController(usecase)
        
        request = HttpRequest(body={"disciplines" : [
                {
                    "name": "Teste",
                    "year": 2020,
                    "students_emails_list": ["22.01102-0@maua.br"],
                },
                {
                    "name": "Teste2",
                    "year": 2020,
                    "students_emails_list": [],
                },
                {
                    "name": "Teste3",
                    "year": 2020,
                }
            ]}                  
        )

        response = controller(request)
        
        assert response.status_code == 201
        assert len(response.body["disciplines"]) == 3
    
    def test_batch_create_disciplines_controller_missing_disciplines(self):
        repo = DisciplineRepositoryMock()
        usecase = BatchCreateDisciplinesUseCase(repo)
        controller = BatchCreateDisciplinesController(usecase)
        
        request = HttpRequest(body={})
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Field disciplines is missing"
        
    def test_batch_create_disciplines_controller_missing_name(self):
        repo = DisciplineRepositoryMock()
        usecase = BatchCreateDisciplinesUseCase(repo)
        controller = BatchCreateDisciplinesController(usecase)
        
        request = HttpRequest(body={"disciplines" : [
                {
                    "year": 2020,
                    "students_emails_list": [],
                }
            ]}
        )
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Field name is missing in discipline 1"
        
    def test_batch_create_disciplines_controller_missing_year(self):
        repo = DisciplineRepositoryMock()
        usecase = BatchCreateDisciplinesUseCase(repo)
        controller = BatchCreateDisciplinesController(usecase)
        
        request = HttpRequest(body={"disciplines" : [
                {
                    "name": "Teste",
                    "students_emails_list": [],
                }
            ]}
        )
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Field year is missing in discipline 1"
        
    def test_batch_create_disciplines_controller_missing_students_emails_list(self):
        repo = DisciplineRepositoryMock()
        usecase = BatchCreateDisciplinesUseCase(repo)
        controller = BatchCreateDisciplinesController(usecase)
        
        request = HttpRequest(body={"disciplines" : [
                {
                    "name": "Teste",
                    "year": 2020,
                }
            ]}
        )
        
        response = controller(request)
        
        assert response.status_code == 201
        assert len(response.body["disciplines"]) == 1
        assert response.body["disciplines"][0]["students_emails_list"] == []
        
    def test_batch_create_disciplines_controller_missing_exercise_id(self):
        repo = DisciplineRepositoryMock()
        usecase = BatchCreateDisciplinesUseCase(repo)
        controller = BatchCreateDisciplinesController(usecase)
        
        request = HttpRequest(body={"disciplines" : [
                {
                    "name": "Teste",
                    "year": 2020,
                    "students_emails_list": [],
                },
                {
                    "name": "Teste2",
                    "year": 2020,
                    "students_emails_list": [],
                },
                {
                    "name": "Teste3",
                    "year": 2020,
                    "students_emails_list": [],
                }
            ]}
        )
        
        response = controller(request)
        
        assert response.status_code == 201
        assert len(response.body["disciplines"]) == 3
        assert response.body["disciplines"][0]["discipline_id"] is not None
        assert response.body["disciplines"][1]["discipline_id"] is not None
        assert response.body["disciplines"][2]["discipline_id"] is not None
        
    def test_batch_create_disciplines_controller_invalid_name(self):
        repo = DisciplineRepositoryMock()
        usecase = BatchCreateDisciplinesUseCase(repo)
        controller = BatchCreateDisciplinesController(usecase)
        
        request = HttpRequest(body={"disciplines" : [
                {
                    "name": 1,
                    "year": 2020,
                    "students_emails_list": [],
                }
            ]}
        )
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid name in discipline 1"
        
    def test_batch_create_disciplines_controller_not_int_year(self):
        repo = DisciplineRepositoryMock()
        usecase = BatchCreateDisciplinesUseCase(repo)
        controller = BatchCreateDisciplinesController(usecase)
        
        request = HttpRequest(body={"disciplines" : [
                {
                    "name": "Teste",
                    "year": "2020",
                    "students_emails_list": [],
                }
            ]}
        )
        
        response = controller(request)
        
        assert response.status_code == 201
        assert len(response.body["disciplines"]) == 1
        assert response.body["disciplines"][0]["year"] == 2020
        
    def test_batch_create_disciplines_controller_invalid_year(self):
        repo = DisciplineRepositoryMock()
        usecase = BatchCreateDisciplinesUseCase(repo)
        controller = BatchCreateDisciplinesController(usecase)
        request = HttpRequest(body={"disciplines" : [
                {
                    "name": "Teste",
                    "year": "aaaa",
                    "students_emails_list": [],
                }
            ]}
        )
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid year in discipline 1"
        
    def test_batch_create_disciplines_controller_invalid_students_emails_list(self):
        repo = DisciplineRepositoryMock()
        usecase = BatchCreateDisciplinesUseCase(repo)
        controller = BatchCreateDisciplinesController(usecase)

        request = HttpRequest(body={"disciplines" : [
                {
                    "name": "Teste",
                    "year": 2020,
                    "students_emails_list": "aaaa",
                }
            ]}
        )
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid students_emails_list in discipline 1"
        
    def test_batch_create_disciplines_controller_invalid_email(self):
        repo = DisciplineRepositoryMock()
        usecase = BatchCreateDisciplinesUseCase(repo)
        controller = BatchCreateDisciplinesController(usecase)

        request = HttpRequest(body={"disciplines" : [
                {
                    "name": "Teste",
                    "year": 2020,
                    "students_emails_list": ["aaaa"],
                }
            ]}
        )
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid email aaaa in discipline 1"