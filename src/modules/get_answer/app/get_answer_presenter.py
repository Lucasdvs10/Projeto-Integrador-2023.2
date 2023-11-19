from .get_answer_controller import GetAnswerController
from .get_answer_usecase import GetAnswerUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


def get_answer_presenter(event, context):
    repo = AnswerRepositoryMock()
    usecase = GetAnswerUsecase(repo)
    controller = GetAnswerController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()