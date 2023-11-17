from fastapi.exceptions import HTTPException
import pytest
from src.modules.get_all_disciplines.app.get_all_disciplines_usecase import GetAllDisciplinesUseCase
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock


class Test_GetAllDisciplinesUseCase:
    def test_get_all_disciplines(self):
        repo = DisciplineRepositoryMock()
        usecase = GetAllDisciplinesUseCase(repo)
        
        all_disciplines = usecase()
        
        assert all_disciplines == repo.all_disciplines
        
    def test_get_all_disciplines_empty(self):
        repo = DisciplineRepositoryMock()
        repo.all_disciplines = []
        usecase = GetAllDisciplinesUseCase(repo)
        
        with pytest.raises(HTTPException) as exc:
            all_disciplines = usecase()
        assert exc.value.status_code == 404
        assert exc.value.detail == "No disciplines found"