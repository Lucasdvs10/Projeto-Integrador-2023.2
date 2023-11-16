from src.modules.batch_create_users.app.batch_create_users_viewmodel import BatchCreateUsersViewmodel
from src.shared.helpers.functions.user_generator import UserGenerator


class Test_BatchCreateUsersViewmodel:
    def test_batch_create_users_viewmodel(self):
        users = UserGenerator.generate_users(5)
        viewmodel = BatchCreateUsersViewmodel(users)
        
        assert len(viewmodel.users) == len(users)
        assert viewmodel.to_dict()["message"] == "Users created successfully"
        assert viewmodel.to_dict()["users"][0]["email"] == users[0].email