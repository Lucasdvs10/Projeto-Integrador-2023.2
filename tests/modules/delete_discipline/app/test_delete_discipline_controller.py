from fastapi.exceptions import HTTPException
import pytest
from src.modules.delete_discipline.app.delete_discipline_controller import DeleteDisciplineController
from src.modules.delete_discipline.app.delete_discipline_usecase import DeleteDisciplineUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock


class Test_DeleteDisciplineController:
    def test_delete_discipline_controller(self):
        repo = DisciplineRepositoryMock()
        usecase = DeleteDisciplineUsecase(repo)
        controller = DeleteDisciplineController(usecase)
        
        request = HttpRequest(body={
            "discipline_id": repo.all_disciplines[0].discipline_id
        })
        
        response = controller(request)
        
        assert response.status_code == 200
        assert response.body["discipline"]["discipline_id"] != repo.all_disciplines[0].discipline_id
        
    def test_delete_discipline_controller_missing_discipline_id(self):
        repo = DisciplineRepositoryMock()
        usecase = DeleteDisciplineUsecase(repo)
        controller = DeleteDisciplineController(usecase)
        
        request = HttpRequest(body={})

        with pytest.raises(HTTPException) as exc:
            controller(request)
            
        assert exc.value.status_code == 400
        assert exc.value.detail == "Missing discipline_id"
                
    def test_delete_discipline_controller_invalid_discipline_id(self):
        repo = DisciplineRepositoryMock()
        usecase = DeleteDisciplineUsecase(repo)
        controller = DeleteDisciplineController(usecase)
        
        request = HttpRequest(body={
            "discipline_id": 123
        })
        
        with pytest.raises(HTTPException) as exc:
            controller(request)
            
        assert exc.value.status_code == 400
        assert exc.value.detail == "Invalid discipline_id"