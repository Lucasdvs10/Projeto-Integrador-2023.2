from src.shared.environments import Environments
from .create_answer_controller import CreateAnswerController
from .create_answer_usecase import CreateAnswerUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse


def create_answer_presenter(event, context):
    answer_repo = Environments.get_answer_repo()()
    exercise_repo = Environments.get_exercise_repo()()
    usecase = CreateAnswerUsecase(answer_repo, exercise_repo)
    controller = CreateAnswerController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()