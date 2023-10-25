from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UserRepositoryMock:
    
    def test_create_user(self):
        repo = UserRepositoryMock()
        new_user = User(email="21.01039-1@maua.br", name="Teste", role=ROLE.STUDENT, password="Teste123", disciplines=[], exercises_solved=[])

        response = repo.create_user(new_user)
        assert new_user == response
        assert repo._users[-1] == new_user
        
    def test_update_user_by_email(self):
        repo = UserRepositoryMock()
        user_email = repo._users[0].email
        new_user = repo.update_user_by_email(email=user_email, new_name="Teste", new_role=ROLE.STUDENT, new_password="Teste123", new_disciplines=[1], new_exercises_solved=[2])

        assert repo._users[0] == new_user
        assert repo._users[0].name == "Teste"
        
    def test_get_user_by_email(self):
        repo = UserRepositoryMock()
        user_email = repo._users[0].email
        user = repo.get_user_by_email(email=user_email)

        assert user == repo._users[0]
        
    def test_delete_user_by_email(self):
        repo = UserRepositoryMock()
        user_email = repo._users[0].email
        user = repo.delete_user_by_email(email=user_email)

        assert user != repo._users[0]
        assert user not in repo._users