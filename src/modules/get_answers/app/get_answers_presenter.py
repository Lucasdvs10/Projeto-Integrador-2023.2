from src.modules.get_answers.app.get_answers_controller import GetAnswersController
from src.modules.get_answers.app.get_answers_usecase import GetAnswersUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


def get_answers_presenter(event, context):
    repo = AnswerRepositoryMock()
    usecase = GetAnswersUsecase(repo)
    controller = GetAnswersController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()