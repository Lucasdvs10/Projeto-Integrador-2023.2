from src.modules.batch_create_disciplines.app.batch_create_disciplines_presenter import batch_create_disciplines_presenter


class Test_BatchCreateDisciplinesPresenter:
    def test_batch_create_disciplines_presenter(self):
        event = {
            "body" : {
                "disciplines" : [
                    {
                        "name": "Teste",
                        "year": 2020,
                        "students_emails_list": [],
                    },
                    {
                        "name": "Teste2",
                        "year": 2020,
                        "students_emails_list": [],
                    }
                ]
            }
        }
        
        response = batch_create_disciplines_presenter(event, None)

        assert response["status_code"] == 201
        assert response["body"]["message"] == "Disciplines created successfully"
        assert len(response["body"]["disciplines"]) == 2