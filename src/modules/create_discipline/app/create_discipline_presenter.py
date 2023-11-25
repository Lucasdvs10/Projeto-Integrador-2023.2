from .create_discipline_controller import CreateDisciplineController
from .create_discipline_usecase import CreateDisciplineUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock


def create_discipline_presenter(event, context):
    repo = DisciplineRepositoryMock()
    usecase = CreateDisciplineUsecase(repo)
    controller = CreateDisciplineController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()