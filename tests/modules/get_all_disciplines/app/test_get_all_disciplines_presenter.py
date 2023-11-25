from src.modules.get_all_disciplines.app.get_all_disciplines_presenter import get_all_disciplines_presenter


class Test_GetAllDisciplinesPresenter:
    def test_get_all_disciplines_presenter(self):
        event = {}
        
        response = get_all_disciplines_presenter(event, None)
        
        assert response["status_code"] == 200
        assert response["body"]["message"] == "Disciplines retrieved successfully"