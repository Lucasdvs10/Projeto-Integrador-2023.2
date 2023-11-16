from src.modules.batch_create_users.app.batch_create_users_presenter import batch_create_users_presenter


class Test_BatchCreateUsersPresenter:
    def test_batch_create_users_presenter(self):
        event = {
            "body" : {
                "users" : [
                    {
                        "EmailMaua": "18.03841-2@maua.br",
                        "Aluno": "Teste",
                        "RG": 525919065
                    },
                    {
                        "EmailMaua": "18.03018-5@maua.br",
                        "Aluno": "Teste2",
                        "RG": 525919066
                    }
                ]
            }
        }
        
        response = batch_create_users_presenter(event, None)

        assert response["status_code"] == 201
        assert response["body"]["message"] == "Users created successfully"