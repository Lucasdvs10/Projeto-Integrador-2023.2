from .validate_answer_controller import ValidateAnswerController
from .validate_answer_usecase import ValidateAnswerUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.environments import Environments

def validate_answer_presenter(event, context):
    answer_repo = Environments.get_answer_repo()()
    user_repo = Environments.get_user_repo()()
    usecase = ValidateAnswerUsecase(answer_repo, user_repo)
    controller = ValidateAnswerController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()