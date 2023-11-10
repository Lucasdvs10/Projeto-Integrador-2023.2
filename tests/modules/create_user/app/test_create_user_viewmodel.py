from src.modules.create_user.app.create_user_usecase import CreateUserUsecase
from src.modules.create_user.app.create_user_viewmodel import CreateUserViewmodel
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_CreateUserViewmodel:
    def test_create_user_viewmodel(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)
        new_user = usecase(email="21.01042-0@maua.br", name="Albert Einstein", role=ROLE.STUDENT, password="12345678")
        viewmodel = CreateUserViewmodel(new_user).to_dict()
        expected = {'user': {'email': '21.01042-0@maua.br', 'name': 'Albert Einstein', 'role': 'STUDENT', 'exercises_solved': []}, 'message': 'User created successfully'}
        
        assert viewmodel == expected