from src.modules.create_user.app.create_user_presenter import create_user_presenter


class Test_CreateUserPresenter:
    def test_create_user_presenter(self):
        event = {
            'body' : {
                'email': '21.01042-0@maua.br', 
                'name': 'Albert Einstein', 
                'role': 'STUDENT',
                'password': '12345678'
            }
        }
        
        response = create_user_presenter(event, None)
        
        expected = {
            'user' : {
                'email': '21.01042-0@maua.br', 
                'name': 'Albert Einstein', 
                'role': 'STUDENT',
                'exercises_solved': []
            },
            'message' : 'User created successfully'
        }
        
        assert response["body"] == expected