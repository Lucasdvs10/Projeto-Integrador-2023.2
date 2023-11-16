from fastapi.exceptions import HTTPException
import pytest
from src.modules.batch_create_users.app.batch_create_users_usecase import BatchCreateUsersUsecase
from src.shared.helpers.functions.user_generator import UserGenerator
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_BatchCreateUsersUsecase:
    def test_batch_create_users(self):
        repo = UserRepositoryMock()
        usecase = BatchCreateUsersUsecase(repo)
        len_before = len(repo.get_all_users())
        new_users = usecase(UserGenerator.generate_users(5))
        
        assert len(repo._users) == len_before + len(new_users)
        
    def test_batch_create_users_with_existing_user(self):
        repo = UserRepositoryMock()
        usecase = BatchCreateUsersUsecase(repo)
        
        with pytest.raises(HTTPException) as exc:
            new_users = usecase(UserGenerator.generate_users(5) + [repo.get_all_users()[0]])
        assert exc.value.status_code == 400
        assert exc.value.detail == f"User with e-mail {repo.get_all_users()[0].email} already exists"
        
    def test_batch_create_users_with_duplicate_user(self):
        repo = UserRepositoryMock()
        usecase = BatchCreateUsersUsecase(repo)
        user = UserGenerator.generate_users(1)[0]
        
        with pytest.raises(HTTPException) as exc:
            new_users = usecase([user, user])
        assert exc.value.status_code == 400
        assert exc.value.detail == f"Duplicate e-mail {user.email}"