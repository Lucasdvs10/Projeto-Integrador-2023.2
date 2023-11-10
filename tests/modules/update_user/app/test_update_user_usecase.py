from src.modules.update_user.app.update_user_usecase import UpdateUserUsecase
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
import copy
from fastapi import HTTPException
import pytest

class Test_UpdateUserUsecase:
    def test_update_user_usecase(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        email = repo.get_all_users()[0].email
        old_user = copy.deepcopy(repo.get_user_by_email(email))
        
        updated_user = usecase(email, new_name="Luizinho", new_role=ROLE.STUDENT, new_password="828328282")
        
        assert old_user != updated_user
        assert repo.get_user_by_email(email) == updated_user
        
    def test_update_user_usecase_with_nonexistent_user(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        email = "21.01923-0@maua.br"
        
        with pytest.raises(HTTPException) as exc:
            usecase(email, new_name="Luizinho", new_role=ROLE.STUDENT, new_password="828328282")
        assert exc.value.status_code == 404
        assert exc.value.detail == "User not found"