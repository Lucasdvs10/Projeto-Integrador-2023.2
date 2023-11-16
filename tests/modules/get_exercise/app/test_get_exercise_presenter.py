from src.modules.get_exercise.app.get_exercise_presenter import get_exercise_presenter


class Test_GetExercisePresenter:
    def test_get_exercise_presenter(self):
        event = {
            'body' : {"exercise_id": "111-111-111"}
        }
        
        response = get_exercise_presenter(event, None)
        
        assert response["status_code"] == 200
        assert response["body"]["message"] == "Exercise retrieved successfully"