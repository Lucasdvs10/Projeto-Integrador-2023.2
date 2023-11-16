from fastapi.exceptions import HTTPException
import pytest
from src.modules.get_exercise.app.get_exercise_controller import GetExerciseController
from src.modules.get_exercise.app.get_exercise_usecase import GetExerciseUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


class Test_GetExerciseController:
    def test_get_exercise_controller(self):
        repo = ExerciseRepositoryMock()
        usecase = GetExerciseUsecase(repo)
        controller = GetExerciseController(usecase)
        request = HttpRequest(body={
            "exercise_id": repo.get_all_exercises()[0].exercise_id
        })
        response = controller(request)
        
        expected = {'exercise': {'exercise_id': '111-111-111', 'title': 'Primeiro Presidente do Brasil', 'enunciado': 'Quem foi o primeiro presidente do Brasil?', 'creation_date': 1673319600000, 'expiration_date': 1676084400000, 'correct_answer': 'Marechal Deodoro'}, 'message': 'Exercise retrieved successfully'}
        
        assert response.status_code == 200
        assert response.body == expected
        
    def test_get_exercise_controller_missing_exercise_id(self):
        repo = ExerciseRepositoryMock()
        usecase = GetExerciseUsecase(repo)
        controller = GetExerciseController(usecase)
        request = HttpRequest(body={})
        
        with pytest.raises(HTTPException) as exc:
            response = controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Missing exercise id"
        
    def test_get_exercise_controller_wrong_exercise_id_type(self):
        repo = ExerciseRepositoryMock()
        usecase = GetExerciseUsecase(repo)
        controller = GetExerciseController(usecase)
        request = HttpRequest(body={
            "exercise_id": 123
        })
        
        with pytest.raises(HTTPException) as exc:
            response = controller(request)
        assert exc.value.status_code == 400
        assert exc.value.detail == "Exercise id must be a string"