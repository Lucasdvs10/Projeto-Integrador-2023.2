from src.modules.get_all_exercises.app.get_all_exercises_controller import GetAllExercisesController
from src.modules.get_all_exercises.app.get_all_exercises_usecase import GetAllExercisesUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


class Test_GetAllExercisesController:
    def test_get_all_exercises_controller(self):
        repo = ExerciseRepositoryMock()
        usecase = GetAllExercisesUsecase(repo)
        controller = GetAllExercisesController(usecase)
        
        response = controller(HttpRequest(body={}))
        
        assert response.status_code == 200
        assert len(response.body["exercises"]) == len(repo._exercises)