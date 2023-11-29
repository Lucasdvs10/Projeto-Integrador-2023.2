from .update_discipline_controller import UpdateDisciplineController
from .update_discipline_usecase import UpdateDisciplineUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.environments import Environments


def update_discipline_presenter(event, context):
    repo = Environments.get_discipline_repo()()
    usecase = UpdateDisciplineUsecase(repo)
    controller = UpdateDisciplineController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()