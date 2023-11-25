from src.modules.create_discipline.app.create_discipline_presenter import create_discipline_presenter


class Test_CreateDisciplinePresenter:
    def test_create_discipline_presenter(self):
        event = {
            'body' : {
                'name': 'Discipline 1',
                'year': 1,
                'students_emails_list': [],
            }
        }
        
        response = create_discipline_presenter(event, None)
        
        assert response["status_code"] == 201
        assert response["body"]["message"] == "Discipline created successfully"
        assert response["body"]["discipline"]["discipline_id"]