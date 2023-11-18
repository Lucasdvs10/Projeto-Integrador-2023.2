import pytest
from src.modules.get_discipline.app.get_discipline_usecase import GetDisciplineUsecase
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock
from fastapi import HTTPException

class Test_GetDisciplineUsecase:
    def test_get_discipline_usecase(self):
        repo = DisciplineRepositoryMock()
        usecase = GetDisciplineUsecase(repo)

        discipline = usecase(repo.all_disciplines[0].discipline_id)
        
        assert discipline == repo.all_disciplines[0]
        
    def test_get_discipline_usecase_not_found(self):
        repo = DisciplineRepositoryMock()
        usecase = GetDisciplineUsecase(repo)

        with pytest.raises(HTTPException) as exc:
            usecase("invalid_id")
        
        assert exc.value.status_code == 404
        assert exc.value.detail == "Discipline not found"