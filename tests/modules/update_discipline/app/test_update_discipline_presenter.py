from src.modules.update_discipline.app.update_discipline_presenter import update_discipline_presenter


class Test_UpdateDisciplinePresenter:
    def test_update_discipline_presenter(self):
        event = {
            "body" : {
            "discipline_id": "aaa-bbb-ccc-ddd",
            "new_name": "New name",
            "new_year": 2,
            "new_students_list": ["22.01102-0@maua.br"]
            }
        }
        
        response = update_discipline_presenter(event, None)
        
        assert response["status_code"] == 200
        assert response["body"] == {'discipline': {'discipline_id': 'aaa-bbb-ccc-ddd', 'name': 'New name', 'year': 2, 'students_emails_list': ['22.01102-0@maua.br']}, 'message': 'Discipline updated successfully'}