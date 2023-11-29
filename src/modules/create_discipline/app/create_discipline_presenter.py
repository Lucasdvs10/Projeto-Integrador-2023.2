from .create_discipline_controller import CreateDisciplineController
from .create_discipline_usecase import CreateDisciplineUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.environments import Environments

def create_discipline_presenter(event, context):
    repo = Environments.get_discipline_repo()()
    usecase = CreateDisciplineUsecase(repo)
    controller = CreateDisciplineController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()