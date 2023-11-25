from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock
from .get_discipline_usecase import GetDisciplineUsecase
from .get_discipline_controller import GetDisciplineController

def get_discipline_presenter(event, context):
    repo = DisciplineRepositoryMock()
    usecase = GetDisciplineUsecase(repo)
    controller = GetDisciplineController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()