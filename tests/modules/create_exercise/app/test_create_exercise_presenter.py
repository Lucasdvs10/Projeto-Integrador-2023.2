from src.modules.create_exercise.app.create_exercise_presenter import create_exercise_presenter


class Test_CreateExercisePresenter:
    def test_create_exercise_presenter(self):
        event = {'body' : {
            "exercise_id": "1",
            "title": "Title",
            "enunciado": "Enunciado",
            "creation_date": "1577847600000",
            "expiration_date": "3387133800000",
            "correct_answer": "Correct answer"
        }}
        
        response = create_exercise_presenter(event, None)
        
        assert response["status_code"] == 201
        assert response["body"]["message"] == "Exercise created successfully"