from src.modules.get_all_exercises.app.get_all_exercises_presenter import get_all_exercises_presenter


class Test_GetAllExercisesPresenter:
    def test_get_all_exercises_presenter(self):
        event = {}
        
        response = get_all_exercises_presenter(event, None)
        
        assert response["status_code"] == 200
        assert response["body"]["message"] == "Exercises retrieved successfully"