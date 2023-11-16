from src.modules.delete_exercise.app.delete_exercise_presenter import delete_exercise_presenter


class Test_DeleteExercisePresenter:
    def test_delete_exercise_presenter(self):
        event = {
            'body' : {"exercise_id": "111-111-111"}
        }
        
        response = delete_exercise_presenter(event, None)
        
        assert response["status_code"] == 200
        assert response["body"]["message"] == "Exercise deleted successfully"