from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.infra.repositories.user_repository_mongo import UserRepositoryMongo
import pytest

class Test_UserRepositoryMongo:
    @pytest.mark.skip(reason="MongoDB is not available")
    def test_create_user(self):
        repo = UserRepositoryMongo()
        new_user = User(email="21.01039-1@maua.br", name="Teste", role=ROLE.STUDENT, password="Teste123", exercises_solved=[])
        
        response = repo.create_user(new_user)
        assert type(response) == User
        assert repo.get_user_by_email(email=new_user.email) == new_user
        
    @pytest.mark.skip(reason="MongoDB is not available")
    def test_get_user_by_email(self):
        repo = UserRepositoryMongo()
        user_email = "21.01039-1@maua.br"
        user = repo.get_user_by_email(email=user_email)
        
        assert type(user) == User
        assert user.email == user_email
        
    @pytest.mark.skip(reason="MongoDB is not available")
    def test_update_user_by_email(self):
        repo = UserRepositoryMongo()
        user_email = "21.01039-1@maua.br"
        new_user = repo.update_user_by_email(email=user_email, new_name="Atualizado", new_role="ADMIN", new_password="NovaSenha123!", new_exercises_solved=[2])
        
        assert type(new_user) == User
        assert new_user.email == user_email
        assert new_user.name == "Atualizado"
     
    @pytest.mark.skip(reason="MongoDB is not available")   
    def test_delete_user_by_email(self):
        repo = UserRepositoryMongo()
        user_email = "21.01039-1@maua.br"
        user = repo.delete_user_by_email(email=user_email)
        
        assert type(user) == User
        assert user.email == user_email
        assert repo.get_user_by_email(email=user_email) == None
        
    @pytest.mark.skip(reason="MongoDB is not available")
    def test_get_all_users(self):
        repo = UserRepositoryMongo()
        users = repo.get_all_users()
        
        assert type(users) == list
        assert type(users[0]) == User
        
    @pytest.mark.skip(reason="MongoDB is not available")
    def test_batch_create_users(self):
        repo = UserRepositoryMongo()
        repo_mock = UserRepositoryMock()
        users = repo_mock.get_all_users()
        len_before = len(repo.get_all_users())
        
        created_users = repo.batch_create_users(users)
        
        assert type(created_users) == list
        assert type(created_users[0]) == User
        assert len(repo.get_all_users()) == len_before + len(users)