from src.modules.get_user.app.get_user_presenter import get_user_presenter


class Test_GetUserPresenter:
    def test_get_user_presenter(self):
        event = {
            'body' : {'email': '22.01102-0@maua.br'}}
        
        response = get_user_presenter(event, None)
        
        expected = {
            'user' : {
                'email': '22.01102-0@maua.br', 
                'name': 'Luigi Trevisan', 
                'role': 'MONITOR',
                'exercises_solved': []
            },
            'message' : 'User retrieved successfully'
        }
        
        assert response["body"] == expected