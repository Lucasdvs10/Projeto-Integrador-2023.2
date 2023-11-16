from src.modules.get_user.app.get_user_usecase import GetUserUsecase
from src.modules.get_user.app.get_user_viewmodel import GetUserViewmodel
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetUserViewmodel:
    def test_get_user_viewmodel(self):
        repo = UserRepositoryMock()
        usecase = GetUserUsecase(repo)
        email = "22.01102-0@maua.br"
        new_user = usecase(email=email)
        viewmodel = GetUserViewmodel(new_user).to_dict()
        expected = {'user': {'email': '22.01102-0@maua.br', 'name': 'Luigi Trevisan', 'role': 'MONITOR', 'exercises_solved': []}, 'message': 'User retrieved successfully'}
        
        assert viewmodel == expected