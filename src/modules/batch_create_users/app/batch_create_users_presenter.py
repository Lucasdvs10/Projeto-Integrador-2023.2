from .batch_create_users_controller import BatchCreateUsersController
from .batch_create_users_usecase import BatchCreateUsersUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.environments import Environments

def batch_create_users_presenter(event, context):
    repo = Environments.get_user_repo()()
    usecase = BatchCreateUsersUsecase(repo)
    controller = BatchCreateUsersController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()