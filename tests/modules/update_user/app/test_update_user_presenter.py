from src.modules.update_user.app.update_user_presenter import update_user_presenter
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateUserPresenter:
    def test_update_user_presenter(self):
        repo = UserRepositoryMock()

        event = {'body' : {
            "email": "22.01102-0@maua.br",
            "new_name": "New Name",
            "new_password": "NewPassword",
            "new_exercises_solved": ["1", "2", "3"]
        }}
        response = update_user_presenter(event, None)
        
        assert response["status_code"] == 200
        assert response["body"] == {
            "user": {
                "email": "22.01102-0@maua.br",
                "name": "New Name",
                "role": "MONITOR",
                "exercises_solved": ["1", "2", "3"]
            },
            "message": "User updated successfully"
        }