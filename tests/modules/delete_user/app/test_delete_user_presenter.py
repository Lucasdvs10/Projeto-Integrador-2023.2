from src.modules.delete_user.app.delete_user_presenter import delete_user_presenter


class Test_DeleteUserPresenter:
    def test_delete_user_presenter(self):
        event = {
            'body' : {'email': '22.01102-0@maua.br'}}
        
        response = delete_user_presenter(event, None)
        
        expected = {
            'user' : {
                'email': '22.01102-0@maua.br', 
                'name': 'Luigi Trevisan', 
                'role': 'MONITOR',
                'exercises_solved': []
            },
            'message' : 'User deleted successfully'
        }
        
        assert response["body"] == expected