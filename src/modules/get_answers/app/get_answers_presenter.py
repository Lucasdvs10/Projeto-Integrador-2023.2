from src.modules.get_answers.app.get_answers_controller import GetAnswersController
from src.modules.get_answers.app.get_answers_usecase import GetAnswersUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse


def get_answers_presenter(event, context):
    repo = Environments.get_answer_repo()()
    usecase = GetAnswersUsecase(repo)
    controller = GetAnswersController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()