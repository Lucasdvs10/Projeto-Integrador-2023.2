from fastapi.exceptions import HTTPException
import pytest
from src.modules.batch_create_users.app.batch_create_users_controller import BatchCreateUsersController
from src.modules.batch_create_users.app.batch_create_users_usecase import BatchCreateUsersUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_BatchCreateUsersController:
    def test_batch_create_users_controller(self):
        repo = UserRepositoryMock()
        usecase = BatchCreateUsersUsecase(repo)
        controller = BatchCreateUsersController(usecase)
        
        request = HttpRequest(body={"users" : [
                {
                    "Exer" : 2023,
                    "Escola" : "CST",
                    "Campus" : "SCS",
                    "PerDisc" : "M",
                    "CdDisc" : "TTI203",
                    "NomeDisc" : "Desenvolvimento Multiplataforma",
                    "CurDisc" : "CIC",
                    "SerDisc" : 2,
                    "RA" : "21.01284-0",
                    "StIniCur": "REG",
                    "StFinCur": "",
                    "StIniDisc": "MAT",
                    "StFinDisc": "",
                    "GrpDisc": 1,
                    "TurDisc": 2,
                    "LabDisc": 2,
                    "RG": 525919065,
                    "Aluno": "Teste",
                    "Email" : "teste@teste.com",
                    "EmailMaua": "21.01284-0@maua.br",
                    "Celular" : 11999999999,
                },
                {
                    "EmailMaua": "18.03841-2@maua.br",
                    "Aluno": "Teste2",
                    "RG" : "525210294",
                    "role": "STUDENT",
                    "password": "Senha123!"
                }
            ]}
        )
        
        response = controller(request)
        
        assert response.status_code == 201
        assert len(response.body["users"]) == 2
        assert response.body["users"][0]["email"] == "21.01284-0@maua.br"
        assert response.body["users"][0]["role"] == "STUDENT"
        assert all([user["exercises_solved"] == [] for user in response.body["users"]])
        
    def test_batch_create_users_controller_missing_users(self):
        repo = UserRepositoryMock()
        usecase = BatchCreateUsersUsecase(repo)
        controller = BatchCreateUsersController(usecase)
        
        request = HttpRequest(body={})
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == 'Field users is missing'
        
    def test_batch_create_users_controller_missing_email(self):
        repo = UserRepositoryMock()
        usecase = BatchCreateUsersUsecase(repo)
        controller = BatchCreateUsersController(usecase)
        
        request = HttpRequest(body={"users" : [
                {
                    "Aluno": "Teste",
                    "RG": 525919065
                }
            ]}
        )
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == 'Field EmailMaua (email) is missing in user 1'
        
    def test_batch_create_users_controller_missing_name(self):
        repo = UserRepositoryMock()
        usecase = BatchCreateUsersUsecase(repo)
        controller = BatchCreateUsersController(usecase)
        
        request = HttpRequest(body={"users" : [
                {
                    "EmailMaua": "18.03841-2@maua.br",
                    "RG": 525919065
                }
            ]}
        )
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == 'Field Aluno (name) is missing in user 1'
        
    def test_batch_create_users_controller_missing_role(self):
        repo = UserRepositoryMock()
        usecase = BatchCreateUsersUsecase(repo)
        controller = BatchCreateUsersController(usecase)
        
        request = HttpRequest(body={"users" : [
                {
                    "EmailMaua": "18.03841-2@maua.br",
                    "Aluno": "Teste",
                    "RG": 525919065
                }
            ]}
        )
        
        response = controller(request)
        
        assert response.status_code == 201
        assert response.body["users"][0]["role"] == "STUDENT"
        
    def test_batch_create_users_controller_missing_password(self):
        repo = UserRepositoryMock()
        usecase = BatchCreateUsersUsecase(repo)
        controller = BatchCreateUsersController(usecase)
        
        request = HttpRequest(body={"users" : [
                {
                    "EmailMaua": "18.03841-2@maua.br",
                    "Aluno": "Teste",
                    "RG": 525919065
                }
            ]}
        )
        
        response = controller(request)

        assert response.status_code == 201
        # viewmodel doesn't return password
        
    def test_batch_create_users_controller_invalid_email(self):
        repo = UserRepositoryMock()
        usecase = BatchCreateUsersUsecase(repo)
        controller = BatchCreateUsersController(usecase)
        
        request = HttpRequest(body={"users" : [
                {
                    "EmailMaua": "18.03841-2",
                    "Aluno": "Teste",
                    "RG": 525919065
                }
            ]}
        )
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == 'Invalid EmailMaua (email) in user 1'
        
    def test_batch_create_users_controller_invalid_name(self):
        repo = UserRepositoryMock()
        usecase = BatchCreateUsersUsecase(repo)
        controller = BatchCreateUsersController(usecase)
        
        request = HttpRequest(body={"users" : [
                {
                    "EmailMaua": "18.03841-2@maua.br",
                    "Aluno": 1,
                    "RG": 525919065
                }
            ]}
        )
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == 'Invalid Aluno (name) in user 1'
        
    def test_batch_create_users_controller_invalid_role(self):
        repo = UserRepositoryMock()
        usecase = BatchCreateUsersUsecase(repo)
        controller = BatchCreateUsersController(usecase)
        
        request = HttpRequest(body={"users" : [
                {
                    "EmailMaua": "18.03841-2@maua.br",
                    "Aluno": "Teste",
                    "RG": 525919065,
                    "role": "TEST"
                }
            ]}
        )
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == 'Invalid role in user 1'
        
    def test_batch_create_users_controller_invalid_password(self):
        repo = UserRepositoryMock()
        usecase = BatchCreateUsersUsecase(repo)
        controller = BatchCreateUsersController(usecase)
        
        request = HttpRequest(body={"users" : [
                {
                    "EmailMaua": "18.03841-2@maua.br",
                    "Aluno": "Teste",
                    "RG": 525919065,
                    "password": "123",
                }
            ]}
        )
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == 'Invalid password in user 1'