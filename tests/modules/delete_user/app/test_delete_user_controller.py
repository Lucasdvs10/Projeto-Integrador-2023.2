import pytest
from fastapi import HTTPException
from src.modules.delete_user.app.delete_user_controller import DeleteUserController
from src.modules.delete_user.app.delete_user_usecase import DeleteUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_DeleteUserController:
    def test_delete_user_controller(self):
        repo = UserRepositoryMock()
        len_before = len(repo.get_all_users())
        usecase = DeleteUserUsecase(repo)
        controller = DeleteUserController(usecase)
        email = repo.get_all_users()[0].email
        
        response = controller(HttpRequest(body={"email": email}))
        
        assert response.status_code == 200
        assert response.body["user"]["email"] == email
        assert len(repo.get_all_users()) == len_before - 1
        
    def test_delete_user_controller_with_invalid_email(self):
        repo = UserRepositoryMock()
        usecase = DeleteUserUsecase(repo)
        controller = DeleteUserController(usecase)
        
        with pytest.raises(HTTPException) as exc:
            controller(HttpRequest(body={"email": "invalid_email"}))
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid email"
        
    def test_delete_user_controller_with_missing_email(self):
        repo = UserRepositoryMock()
        usecase = DeleteUserUsecase(repo)
        controller = DeleteUserController(usecase)
        
        with pytest.raises(HTTPException) as exc:
            controller(HttpRequest(body={"invalid_field": "invalid_email"}))
        assert exc.value.status_code == 400
        assert exc.value.detail == "Missing email"