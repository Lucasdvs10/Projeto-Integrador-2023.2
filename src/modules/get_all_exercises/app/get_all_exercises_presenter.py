from .get_all_exercises_controller import GetAllExercisesController
from .get_all_exercises_usecase import GetAllExercisesUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


def get_all_exercises_presenter(event, context):
    repo = ExerciseRepositoryMock()
    usecase = GetAllExercisesUsecase(repo)
    controller = GetAllExercisesController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()