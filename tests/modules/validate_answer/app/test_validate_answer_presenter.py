from src.modules.validate_answer.app.validate_answer_presenter import validate_answer_presenter


class Test_ValidateAnswerPresenter:
    def test_validate_answer_presenter(self):
        event = {
            "body" : {
                "answer_id": "0",
                "is_right": 1
            }
        }
        
        response = validate_answer_presenter(event, None)
        
        assert response["status_code"] == 200
        assert response["body"]["message"] == "Answer validated successfully"