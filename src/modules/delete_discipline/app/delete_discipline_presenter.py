from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.environments import Environments
from .delete_discipline_usecase import DeleteDisciplineUsecase
from .delete_discipline_controller import DeleteDisciplineController

def delete_discipline_presenter(event, context):
    repo = Environments.get_discipline_repo()()
    usecase = DeleteDisciplineUsecase(repo)
    controller = DeleteDisciplineController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()