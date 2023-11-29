from src.shared.environments import Environments
from .create_answer_controller import CreateAnswerController
from .create_answer_usecase import CreateAnswerUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


def create_answer_presenter(event, context):
    repo = Environments.get_answer_repo()()
    usecase = CreateAnswerUsecase(repo)
    controller = CreateAnswerController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()