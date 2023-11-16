from fastapi.exceptions import HTTPException
import pytest
from src.modules.update_exercise.app.update_exercise_controller import UpdateExerciseController
from src.modules.update_exercise.app.update_exercise_usecase import UpdateExerciseUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock
from fastapi.exceptions import HTTPException
import pytest
from src.modules.update_exercise.app.update_exercise_controller import UpdateExerciseController
from src.modules.update_exercise.app.update_exercise_usecase import UpdateExerciseUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


class Test_UpdateExerciseController:
    def test_update_exercise_controller(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": "New title",
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        response = controller(httpRequest)
        
        assert response.status_code == 200
        assert response.body == {'exercise': {'exercise_id': exercise_id, 'title': 'New title', 'enunciado': 'New enunciado', 'creation_date': 1577847600000, 'expiration_date': 3387133800000, 'correct_answer': 'New correct answer'}, 'message': 'Exercise updated successfully'}
        
    def test_update_exercise_controller_missing_exercise_id(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        httpRequest = HttpRequest(body={
            "new_title": "New title",
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "Missing exercise_id"
        
    def test_update_exercise_controller_invalid_exercise_id(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        httpRequest = HttpRequest(body={
            "exercise_id": 1,
            "new_title": "New title",
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid exercise_id"
        
    def test_update_exercise_controller_none_new_title(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": None,
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "Title can't be None"
        
    def test_update_exercise_controller_invalid_new_title_type(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": 1,
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "New title must be a string"
        
    def test_update_exercise_controller_invalid_new_title_length(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": "a",
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == f"New title must be between 3 and 150 characters"
      
    def test_update_exercise_controller_none_new_enunciado(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": "New title",
            "new_enunciado": None,
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "Enunciado can't be None"
        
    def test_update_exercise_controller_invalid_new_enunciado_type(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": "New title",
            "new_enunciado": 1,
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "New enunciado must be a string"
        
    def test_update_exercise_controller_invalid_new_enunciado_length(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": "New title",
            "new_enunciado": "a",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == f"New enunciado must be between 3 and 500 characters"
        
    def test_update_exercise_controller_none_new_creation_date(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": "New title",
            "new_enunciado": "New enunciado",
            "new_creation_date": None,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "Creation date can't be None"
        
    def test_update_exercise_controller_invalid_new_creation_date_type(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": "New title",
            "new_enunciado": "New enunciado",
            "new_creation_date": "invalid_date",
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "New creation date must be an integer"
        
    def test_update_exercise_controller_invalid_new_creation_date_range(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": "New title",
            "new_enunciado": "New enunciado",
            "new_creation_date": 1000000000000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "New creation date must be between 2020-01-01 and 2077-05-01"
        
    def test_update_exercise_controller_none_new_expiration_date(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": "New title",
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": None,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "Expiration date can't be None"
        
    def test_update_exercise_controller_invalid_new_expiration_date_type(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": "New title",
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": "invalid_date",
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "New expiration date must be an integer"
        
    def test_update_exercise_controller_invalid_new_expiration_date_range(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": "New title",
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 5000000000000,
            "new_correct_answer": "New correct answer"
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "New expiration date must be between 2020-01-01 and 2077-05-01"
        
    def test_update_exercise_controller_none_new_correct_answer(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": "New title",
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": None
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "Correct answer can't be None"
        
    def test_update_exercise_controller_invalid_new_correct_answer_type(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": "New title",
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": 1
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "New correct answer must be a string"
        
    def test_update_exercise_controller_empty_new_correct_answer(self):
        repo = ExerciseRepositoryMock()
        usecase = UpdateExerciseUsecase(repo)
        controller = UpdateExerciseController(usecase)
        exercise_id = repo.get_all_exercises()[0].exercise_id
        httpRequest = HttpRequest(body={
            "exercise_id": exercise_id,
            "new_title": "New title",
            "new_enunciado": "New enunciado",
            "new_creation_date": 1577847600000,
            "new_expiration_date": 3387133800000,
            "new_correct_answer": ""
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(httpRequest)
        
        assert exc.value.status_code == 400
        assert exc.value.detail == "New correct answer can't be empty"