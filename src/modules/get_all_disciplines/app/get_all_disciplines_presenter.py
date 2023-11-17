from .get_all_disciplines_controller import GetAllDisciplinesController
from .get_all_disciplines_usecase import GetAllDisciplinesUseCase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock


def get_all_disciplines_presenter(event, context):
    repo = DisciplineRepositoryMock()
    usecase = GetAllDisciplinesUseCase(repo)
    controller = GetAllDisciplinesController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()