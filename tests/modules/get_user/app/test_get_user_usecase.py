from fastapi import HTTPException
import pytest
from src.modules.get_user.app.get_user_usecase import GetUserUsecase
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetUserUsecase:
    def test_get_user_usecase(self):
        repo = UserRepositoryMock()
        usecase = GetUserUsecase(repo)
        test_user = repo.get_all_users()[0]
        user = usecase(email=test_user.email)
        
        assert user == test_user

    def test_get_user_usecase_not_found(self):
        repo = UserRepositoryMock()
        usecase = GetUserUsecase(repo)
        
        with pytest.raises(HTTPException) as exc:
            usecase(email="15.02134-2@maua.br")
        assert exc.value.status_code == 404
        assert exc.value.detail == "User not found"