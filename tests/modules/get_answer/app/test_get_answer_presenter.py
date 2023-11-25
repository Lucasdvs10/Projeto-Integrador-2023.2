from src.modules.get_answer.app.get_answer_presenter import get_answer_presenter


class Test_GetAnswerPresenter:
    def test_get_answer_presenter(self):
        event = {
            'body' : {"answer_id": "0"}
        }
        
        response = get_answer_presenter(event, None)
        
        assert response["status_code"] == 200
        assert response["body"]["message"] == "Answer retrieved successfully"