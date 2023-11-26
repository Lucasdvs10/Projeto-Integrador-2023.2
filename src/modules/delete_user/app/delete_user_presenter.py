from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from .delete_user_usecase import DeleteUserUsecase
from .delete_user_controller import DeleteUserController
from src.shared.environments import Environments

def delete_user_presenter(event, context):
    repo = Environments.get_user_repo()()
    usecase = DeleteUserUsecase(repo)
    controller = DeleteUserController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()