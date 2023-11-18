from fastapi.exceptions import HTTPException
import pytest
from src.modules.get_discipline.app.get_discipline_controller import GetDisciplineController
from src.modules.get_discipline.app.get_discipline_usecase import GetDisciplineUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock


class Test_GetDisciplineController:
    def test_get_discipline_controller(self):
        repo = DisciplineRepositoryMock()
        usecase = GetDisciplineUsecase(repo)
        controller = GetDisciplineController(usecase)
        
        request = HttpRequest(body={
            "discipline_id": repo.all_disciplines[0].discipline_id
        })
        
        response = controller(request)
        
        assert response.status_code == 200
        assert response.body["discipline"]["discipline_id"] == repo.all_disciplines[0].discipline_id
        
    def test_get_discipline_controller_missing_discipline_id(self):
        repo = DisciplineRepositoryMock()
        usecase = GetDisciplineUsecase(repo)
        controller = GetDisciplineController(usecase)
        
        request = HttpRequest(body={})

        with pytest.raises(HTTPException) as exc:
            controller(request)
            
        assert exc.value.status_code == 400
        assert exc.value.detail == "Missing discipline_id"
                
    def test_get_discipline_controller_invalid_discipline_id(self):
        repo = DisciplineRepositoryMock()
        usecase = GetDisciplineUsecase(repo)
        controller = GetDisciplineController(usecase)
        
        request = HttpRequest(body={
            "discipline_id": 123
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
            
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid discipline_id"