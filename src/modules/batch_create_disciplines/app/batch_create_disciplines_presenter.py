from .batch_create_disciplines_controller import BatchCreateDisciplinesController
from .batch_create_disciplines_usecase import BatchCreateDisciplinesUseCase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.environments import Environments


def batch_create_disciplines_presenter(event, context):
    repo = Environments.get_discipline_repo()()
    usecase = BatchCreateDisciplinesUseCase(repo)
    controller = BatchCreateDisciplinesController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()