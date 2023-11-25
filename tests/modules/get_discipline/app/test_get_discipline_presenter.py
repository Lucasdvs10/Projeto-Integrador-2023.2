from src.modules.get_discipline.app.get_discipline_presenter import get_discipline_presenter


class Test_GetDisciplinePresenter:
    def test_get_discipline_presenter(self):
        event = {
            'body' : {'discipline_id': 'aaa-bbb-ccc-ddd'}}
        
        response = get_discipline_presenter(event, None)
        
        expected = {
            'discipline' : {
                'name': 'Calculo 1', 
                'discipline_id': 'aaa-bbb-ccc-ddd', 
                'year': 2, 
                'students_emails_list': ['umemail@gmail.com']
            },
            'message' : 'Discipline retrieved successfully'
        }
        
        assert response["body"] == expected