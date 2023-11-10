from src.modules.delete_user.app.delete_user_usecase import DeleteUserUsecase
from src.modules.delete_user.app.delete_user_viewmodel import DeleteUserViewmodel
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_DeleteUserViewmodel:
    def test_delete_user_viewmodel(self):
        repo = UserRepositoryMock()
        usecase = DeleteUserUsecase(repo)
        email = repo.get_all_users()[0].email
        new_user = usecase(email=email)
        viewmodel = DeleteUserViewmodel(new_user).to_dict()
        expected = {'user': {'email': '22.01102-0@maua.br', 'name': 'Luigi Trevisan', 'role': 'MONITOR', 'exercises_solved': []}, 'message': 'User deleted successfully'}
        
        assert viewmodel == expected