from .create_user_controller import CreateUserController
from .create_user_usecase import CreateUserUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


def create_user_presenter(event, context):
    repo = UserRepositoryMock()
    usecase = CreateUserUsecase(repo)
    controller = CreateUserController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()