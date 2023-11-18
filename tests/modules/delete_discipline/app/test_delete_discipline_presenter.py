from src.modules.delete_discipline.app.delete_discipline_presenter import delete_discipline_presenter


class Test_DeleteDisciplinePresenter:
    def test_delete_discipline_presenter(self):
        event = {
            'body' : {'discipline_id': 'aaa-bbb-ccc-ddd'}}
        
        response = delete_discipline_presenter(event, None)
        
        expected = {
            'discipline' : {
                'name': 'Calculo 1', 
                'discipline_id': 'aaa-bbb-ccc-ddd', 
                'year': 2, 
                'students_emails_list': ['umemail@gmail.com']
            },
            'message' : 'Discipline deleted successfully'
        }
        
        assert response["body"] == expected