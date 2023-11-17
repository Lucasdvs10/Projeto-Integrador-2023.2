from src.modules.get_all_disciplines.app.get_all_disciplines_controller import GetAllDisciplinesController
from src.modules.get_all_disciplines.app.get_all_disciplines_usecase import GetAllDisciplinesUseCase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock


class Test_GetAllDisciplinesController:
    def test_get_all_disciplines_controller(self):
        repo = DisciplineRepositoryMock()
        usecase = GetAllDisciplinesUseCase(repo)
        controller = GetAllDisciplinesController(usecase)
        
        response = controller(HttpRequest(body={}))
        
        assert response.status_code == 200
        assert len(response.body["disciplines"]) == len(repo.all_disciplines)