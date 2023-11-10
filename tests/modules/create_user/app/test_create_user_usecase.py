from fastapi import HTTPException
import pytest
from src.modules.create_user.app.create_user_usecase import CreateUserUsecase
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_CreateUserUsecase:
    def test_create_user_usecase(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)
        len_before = len(repo.get_all_users())
        new_user = usecase(email="21.01042-0@maua.br", name="Albert Einstein", role=ROLE.STUDENT, password="12345678")
        
        assert len(repo.get_all_users()) == len_before + 1
        assert new_user == repo.get_user_by_email("21.01042-0@maua.br")
        assert repo.get_all_users()[-1] == new_user
        
    def test_create_user_usecase_already_registered(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)
        email = repo.get_all_users()[0].email
        with pytest.raises(HTTPException) as exc:
            usecase(email=email, name="Albert Einstein", role=ROLE.STUDENT, password="12345678")
        assert exc.value.status_code == 409
        assert exc.value.detail == "Email already registered"