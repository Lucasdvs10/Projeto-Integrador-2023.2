from .get_exercise_controller import GetExerciseController
from .get_exercise_usecase import GetExerciseUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


def get_exercise_presenter(event, context):
    repo = ExerciseRepositoryMock()
    usecase = GetExerciseUsecase(repo)
    controller = GetExerciseController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()