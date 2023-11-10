from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from .delete_user_usecase import DeleteUserUsecase
from .delete_user_controller import DeleteUserController

def delete_user_presenter(event, context):
    repo = UserRepositoryMock()
    usecase = DeleteUserUsecase(repo)
    controller = DeleteUserController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()