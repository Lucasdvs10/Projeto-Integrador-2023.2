from fastapi import HTTPException
import pytest
from src.modules.delete_user.app.delete_user_usecase import DeleteUserUsecase
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_DeleteUserUsecase:
    def test_delete_user_usecase(self):
        repo = UserRepositoryMock()
        usecase = DeleteUserUsecase(repo)
        user = repo.get_all_users()[0]
        len_before = len(repo.get_all_users())
        
        deleted_user = usecase(user.email)
        
        assert deleted_user == user
        assert len(repo.get_all_users()) == len_before - 1
        assert deleted_user not in repo.get_all_users()
        
    def test_delete_user_usecase_user_not_found(self):
        repo = UserRepositoryMock()
        usecase = DeleteUserUsecase(repo)
        user = repo.get_all_users()[0]
        
        with pytest.raises(HTTPException) as exc:
            deleted_user = usecase("bigodigao@maua.br")
        assert exc.value.status_code == 404
        assert exc.value.detail == "User not found"