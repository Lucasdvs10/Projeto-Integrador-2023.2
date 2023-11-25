from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock
from .delete_discipline_usecase import DeleteDisciplineUsecase
from .delete_discipline_controller import DeleteDisciplineController

def delete_discipline_presenter(event, context):
    repo = DisciplineRepositoryMock()
    usecase = DeleteDisciplineUsecase(repo)
    controller = DeleteDisciplineController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        body=response.body, status_code=response.status_code, headers=response.headers
    )
    
    return httpResponse.to_dict()