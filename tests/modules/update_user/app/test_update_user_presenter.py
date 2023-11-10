from src.modules.update_user.app.update_user_controller import UpdateUserController
from src.modules.update_user.app.update_user_usecase import UpdateUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateUserPresenter:
    def test_update_user_presenter(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        controller = UpdateUserController(usecase)

        httpRequest = HttpRequest(body={
            "email": "22.01102-0@maua.br",
            "new_name": "New Name",
            "new_password": "NewPassword",
            "new_exercises_solved": ["1", "2", "3"]
        })
        response = controller(httpRequest)
        
        assert response.status_code == 200
        assert response.body == {
            "user": {
                "email": "22.01102-0@maua.br",
                "name": "New Name",
                "role": "MONITOR",
                "exercises_solved": ["1", "2", "3"]
            },
            "message": "User updated successfully"
        }