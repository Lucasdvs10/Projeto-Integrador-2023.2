from .update_user_controller import UpdateUserController
from .update_user_usecase import UpdateUserUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.environments import Environments

def update_user_presenter(event, context):
    repo = Environments.get_user_repo()()
    usecase = UpdateUserUsecase(repo)
    controller = UpdateUserController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()