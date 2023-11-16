from src.modules.update_user.app.update_user_usecase import UpdateUserUsecase
from src.modules.update_user.app.update_user_viewmodel import UpdateUserViewmodel
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateUserViewmodel:
    def test_update_user_viewmodel(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        email = "22.01102-0@maua.br"
        updated_user = usecase(email=email, new_name="Luizinho")
        viewmodel = UpdateUserViewmodel(updated_user).to_dict()
        expected = {'user': {'email': '22.01102-0@maua.br', 'name': 'Luizinho', 'role': 'MONITOR', 'exercises_solved': []}, 'message': 'User updated successfully'}
        
        assert viewmodel == expected