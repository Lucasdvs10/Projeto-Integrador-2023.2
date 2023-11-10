from src.modules.update_user.app.update_user_controller import UpdateUserController
from src.modules.update_user.app.update_user_usecase import UpdateUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
import pytest
from fastapi import HTTPException

class Test_UpdateUserController:
    def test_update_user_controller(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        controller = UpdateUserController(usecase)

        response = controller(request=HttpRequest(body={
            "email": "22.01102-0@maua.br",
            "new_name": "New Name",
            "new_password": "NewPassword",
            "new_exercises_solved": ["1", "2", "3"]
        }))
        
        assert response.status_code == 200
        assert response.body == {
            "user": {
                "email": "22.01102-0@maua.br",
                "name": "New Name",
                "role": "MONITOR",
                "exercises_solved": ["1", "2", "3"]
            },
            "message": "User updated successfully"
        }
        
    def test_update_user_controller_with_missing_email(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        controller = UpdateUserController(usecase)

        with pytest.raises(HTTPException) as exc:
            controller(request=HttpRequest(body={
                "new_name": "New Name",
                "new_role": "STUDENT",
                "new_password": "NewPassword",
                "new_exercises_solved": ["1", "2", "3"]
            }))
        assert exc.value.status_code == 400
        assert exc.value.detail == "Missing email"
        
    def test_update_user_controller_with_invalid_email(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        controller = UpdateUserController(usecase)

        with pytest.raises(HTTPException) as exc:
            controller(request=HttpRequest(body={
                "email": "22.01102-0maua.br",
                "new_name": "New Name",
                "new_role": "STUDENT",
                "new_password": "NewPassword",
                "new_exercises_solved": ["1", "2", "3"]
            }))
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid email"
        
    def test_update_user_controller_with_none_new_name(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        controller = UpdateUserController(usecase)

        with pytest.raises(HTTPException) as exc:
            controller(request=HttpRequest(body={
                "email": "22.01102-0@maua.br",
                "new_name": None,
                "new_role": "STUDENT",
                "new_password": "NewPassword",
                "new_exercises_solved": ["1", "2", "3"]
            }))
        assert exc.value.status_code == 400
        assert exc.value.detail == "Name can't be None"
        
    def test_update_user_controller_with_invalid_new_name(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        controller = UpdateUserController(usecase)

        with pytest.raises(HTTPException) as exc:
            controller(request=HttpRequest(body={
                "email": "22.01102-0@maua.br",
                "new_name": 42,
                "new_role": "STUDENT",
                "new_password": "NewPassword",
                "new_exercises_solved": ["1", "2", "3"]
            }))
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid new name"
        
    def test_update_user_controller_with_none_new_role(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        controller = UpdateUserController(usecase)

        with pytest.raises(HTTPException) as exc:
            controller(request=HttpRequest(body={
                "email": "22.01102-0@maua.br",
                "new_name": "New Name",
                "new_role": None,
                "new_password": "NewPassword",
                "new_exercises_solved": ["1", "2", "3"]
            }))
        assert exc.value.status_code == 400
        assert exc.value.detail == "Role can't be None"
        
    def test_update_user_controller_with_invalid_new_role(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        controller = UpdateUserController(usecase)

        with pytest.raises(HTTPException) as exc:
            controller(request=HttpRequest(body={
                "email": "22.01102-0@maua.br",
                "new_name": "New Name",
                "new_role": "INVALID_ROLE",
                "new_password": "NewPassword",
                "new_exercises_solved": ["1", "2", "3"]
            }))
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid role"
        
    def test_update_user_controller_with_none_new_password(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        controller = UpdateUserController(usecase)

        with pytest.raises(HTTPException) as exc:
            controller(request=HttpRequest(body={
                "email": "22.01102-0@maua.br",
                "new_name": "New Name",
                "new_role": "STUDENT",
                "new_password": None,
                "new_exercises_solved": ["1", "2", "3"]
            }))
        assert exc.value.status_code == 400
        assert exc.value.detail == "Password can't be None"
        
    def test_update_user_controller_with_invalid_new_password(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        controller = UpdateUserController(usecase)

        with pytest.raises(HTTPException) as exc:
            controller(request=HttpRequest(body={
                "email": "22.01102-0@maua.br",
                "new_name": "New Name",
                "new_role": "STUDENT",
                "new_password": 1,
                "new_exercises_solved": ["1", "2", "3"]
            }))
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid new password"
        
    def test_update_user_controller_with_invalid_new_exercises_solved(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        controller = UpdateUserController(usecase)

        with pytest.raises(HTTPException) as exc:
            controller(request=HttpRequest(body={
                "email": "22.01102-0@maua.br",
                "new_name": "New Name",
                "new_role": "STUDENT",
                "new_password": "NewPassword",
                "new_exercises_solved": "invalid_exercises_solved"
            }))
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid new exercises solved"
        
    def test_update_user_controller_with_invalid_new_exercises_solved_type(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        controller = UpdateUserController(usecase)

        with pytest.raises(HTTPException) as exc:
            controller(request=HttpRequest(body={
                "email": "22.01102-0@maua.br",
                "new_name": "New Name",
                "new_role": "STUDENT",
                "new_password": "NewPassword",
                "new_exercises_solved": [1, 2, 3]
            }))
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid new exercises solved"
        
    def test_update_user_controller_with_invalid_new_exercises_solved_values(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        controller = UpdateUserController(usecase)

        with pytest.raises(HTTPException) as exc:
            controller(request=HttpRequest(body={
                "email": "22.01102-0@maua.br",
                "new_name": "New Name",
                "new_role": "STUDENT",
                "new_password": "NewPassword",
                "new_exercises_solved": ["1", 2, "3"]
            }))
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid new exercises solved"