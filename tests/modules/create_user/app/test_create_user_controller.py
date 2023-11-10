from fastapi import HTTPException
import pytest
from src.modules.create_user.app.create_user_controller import CreateUserController
from src.modules.create_user.app.create_user_usecase import CreateUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_CreateUserController:
    def test_create_user_controller(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)
        controller = CreateUserController(usecase)
        
        request = HttpRequest(
            body={'email': '21.01042-0@maua.br', 
            'name': 'Albert Einstein', 
            'role': 'STUDENT',
            'password': '12345678'})
        
        response = controller(request)
        assert response.status_code == 201
        assert response.body == {
            'user': {
                'email' : '21.01042-0@maua.br',
                'name' : 'Albert Einstein',
                'role' : 'STUDENT',
                'exercises_solved' : []
            },
            'message' : 'User created successfully'
        }
        
    def test_create_user_controller_missing_email(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)
        controller = CreateUserController(usecase)
        
        request = HttpRequest(
            body={'name': 'Albert Einstein', 
            'role': 'STUDENT',
            'password': '12345678'})
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == 'Field email is missing'
        
    def test_create_user_controller_invalid_email(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)
        controller = CreateUserController(usecase)
        
        request = HttpRequest(
            body={'email': '21.01042-0maua.br', 
            'name': 'Albert Einstein', 
            'role': 'STUDENT',
            'password': '12345678'})
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == 'Invalid email'
        
    def test_create_user_controller_missing_name(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)
        controller = CreateUserController(usecase)
        
        request = HttpRequest(
            body={'email': '21.01042-0@maua.br', 
            'role': 'STUDENT',
            'password': '12345678'})
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == 'Field name is missing'
        
    def test_create_user_controller_invalid_name(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)
        controller = CreateUserController(usecase)
        
        request = HttpRequest(
            body={'email': '21.01042-0@maua.br', 
            'name': 1, 
            'role': 'STUDENT',
            'password': '12345678'})
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == 'Invalid name'
        
    def test_create_user_controller_missing_role(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)
        controller = CreateUserController(usecase)
        
        request = HttpRequest(
            body={'email': '21.01042-0@maua.br', 
            'name': 'Albert Einstein', 
            'password': '12345678'})
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == 'Field role is missing'
        
    def test_create_user_controller_invalid_role(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)
        controller = CreateUserController(usecase)
        
        request = HttpRequest(
            body={'email': '21.01042-0@maua.br', 
            'name': 'Albert Einstein', 
            'role': 'WHATSAPP',
            'password': '12345678'})
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == 'Invalid role'
        
    def test_create_user_controller_missing_password(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)
        controller = CreateUserController(usecase)
        
        request = HttpRequest(
            body={'email': '21.01042-0@maua.br', 
            'name': 'Albert Einstein', 
            'role': 'STUDENT'})
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == 'Field password is missing'
        
    def test_create_user_controller_invalid_password(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)
        controller = CreateUserController(usecase)
        
        request = HttpRequest(
            body={'email': '21.01042-0@maua.br', 
            'name': 'Albert Einstein', 
            'role': 'STUDENT',
            'password': '1234'})
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == 'Invalid password'