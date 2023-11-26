from src.shared.environments import Environments
from .delete_exercise_controller import DeleteExerciseController
from .delete_exercise_usecase import DeleteExerciseUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse


def delete_exercise_presenter(event, context):
    repo = Environments.get_exercise_repo()()
    usecase = DeleteExerciseUsecase(repo)
    controller = DeleteExerciseController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()