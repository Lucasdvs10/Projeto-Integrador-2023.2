from fastapi.exceptions import HTTPException
import pytest
from src.modules.create_exercise.app.create_exercise_controller import CreateExerciseController
from src.modules.create_exercise.app.create_exercise_usecase import CreateExerciseUseCase
from src.shared.domain.entities.exercise import Exercise
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


class Test_CreateExerciseController:
    def test_create_exercise_controller(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "title": "Exercise 1",
            "enunciado": "Enunciado 1",
            "creation_date": "1577847600000",
            "expiration_date": "3387133800000",
            "correct_answer": "Answer 1"
        })
        
        response = controller(request)
        assert response.status_code == 201
        assert response.body == {
            "exercise": {
                "exercise_id": "1",
                "title": "Exercise 1",
                "enunciado": "Enunciado 1",
                "creation_date": 1577847600000,
                "expiration_date": 3387133800000,
                "correct_answer": "Answer 1"
            },
            "message": "Exercise created successfully"
        }
        
    def test_create_exercise_controller_missing_exercise_id(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "title": "Exercise 1",
            "enunciado": "Enunciado 1",
            "creation_date": "1577847600000",
            "expiration_date": "3387133800000",
            "correct_answer": "Answer 1"
        })
        
        response = controller(request)
        
        assert response.status_code == 201
        assert response.body["exercise"]["exercise_id"]
        
    def test_create_exercise_controller_invalid_exercise_id(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": 1,
            "title": "Exercise 1",
            "enunciado": "Enunciado 1",
            "creation_date": "1577847600000",
            "expiration_date": "3387133800000",
            "correct_answer": "Answer 1"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Exercise id must be a string"
        
    def test_create_exercise_controller_missing_title(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "enunciado": "Enunciado 1",
            "creation_date": "1577847600000",
            "expiration_date": "3387133800000",
            "correct_answer": "Answer 1"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Title is required"
        
    def test_create_exercise_controller_invalid_title(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "title": 1,
            "enunciado": "Enunciado 1",
            "creation_date": "1577847600000",
            "expiration_date": "3387133800000",
            "correct_answer": "Answer 1"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Title must be a string"
        
    def test_create_exercise_controller_invalid_title_length(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "title": "a",
            "enunciado": "Enunciado 1",
            "creation_date": "1577847600000",
            "expiration_date": "3387133800000",
            "correct_answer": "Answer 1"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == f"Title must have between {Exercise.MIN_TITLE_LENGTH} and {Exercise.MAX_TITLE_LENGTH} characters"
        
    def test_create_exercise_controller_missing_enunciado(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "title": "Exercise 1",
            "creation_date": "1577847600000",
            "expiration_date": "3387133800000",
            "correct_answer": "Answer 1"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Enunciado is required"
        
    def test_create_exercise_controller_invalid_enunciado(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "title": "Exercise 1",
            "enunciado": 1,
            "creation_date": "1577847600000",
            "expiration_date": "3387133800000",
            "correct_answer": "Answer 1"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Enunciado must be a string"
        
    def test_create_exercise_controller_invalid_enunciado_length(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "title": "Exercise 1",
            "enunciado": "a",
            "creation_date": "1577847600000",
            "expiration_date": "3387133800000",
            "correct_answer": "Answer 1"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == f"Enunciado must have between {Exercise.MIN_ENUNCIADO_LENGTH} and {Exercise.MAX_ENUNCIADO_LENGTH} characters"
        
    def test_create_exercise_controller_missing_creation_date(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "title": "Exercise 1",
            "enunciado": "Enunciado 1",
            "expiration_date": "3387133800000",
            "correct_answer": "Answer 1"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Creation date is required"
        
    def test_create_exercise_controller_invalid_creation_date(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "title": "Exercise 1",
            "enunciado": "Enunciado 1",
            "creation_date": "invalid_date",
            "expiration_date": "3387133800000",
            "correct_answer": "Answer 1"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Creation date must be a decimal string"
        
    def test_create_exercise_controller_invalid_creation_date_range(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "title": "Exercise 1",
            "enunciado": "Enunciado 1",
            "creation_date": "1577847599999",
            "expiration_date": "3387133800000",
            "correct_answer": "Answer 1"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Creation date must be between 2020-01-01 and 2077-05-01"
        
    def test_create_exercise_controller_missing_expiration_date(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "title": "Exercise 1",
            "enunciado": "Enunciado 1",
            "creation_date": "1577847600000",
            "correct_answer": "Answer 1"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Expiration date is required"
        
    def test_create_exercise_controller_invalid_expiration_date(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "title": "Exercise 1",
            "enunciado": "Enunciado 1",
            "creation_date": "1577847600000",
            "expiration_date": "invalid_date",
            "correct_answer": "Answer 1"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Expiration date must be a decimal string"
        
    def test_create_exercise_controller_invalid_expiration_date_range(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "title": "Exercise 1",
            "enunciado": "Enunciado 1",
            "creation_date": "1577847600000",
            "expiration_date": "3387133800001",
            "correct_answer": "Answer 1"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Expiration date must be between 2020-01-01 and 2077-05-01"
        
    def test_create_exercise_controller_expiration_date_before_creation_date(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "title": "Exercise 1",
            "enunciado": "Enunciado 1",
            "creation_date": "3387133800000",
            "expiration_date": "1577847600000",
            "correct_answer": "Answer 1"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Expiration date must be after creation date"
        
    def test_create_exercise_controller_missing_correct_answer(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "title": "Exercise 1",
            "enunciado": "Enunciado 1",
            "creation_date": "1577847600000",
            "expiration_date": "3387133800000",
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Correct answer is required"
        
    def test_create_exercise_controller_invalid_correct_answer(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        controller = CreateExerciseController(usecase)
        
        request = HttpRequest(body={
            "exercise_id": "1",
            "title": "Exercise 1",
            "enunciado": "Enunciado 1",
            "creation_date": "1577847600000",
            "expiration_date": "3387133800000",
            "correct_answer": 1
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Correct answer must be a string"