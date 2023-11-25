from src.modules.delete_discipline.app.delete_discipline_usecase import DeleteDisciplineUsecase
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock
import pytest
from fastapi import HTTPException

class Test_DeleteDisciplineUsecase:
    def test_delete_discipline_usecase(self):
        repo = DisciplineRepositoryMock()
        usecase = DeleteDisciplineUsecase(repo)
        discipline_id = repo.all_disciplines[0].discipline_id
        len_before = len(repo.all_disciplines)
        deleted_discipline = usecase(discipline_id)

        assert deleted_discipline.discipline_id == discipline_id
        assert len(repo.all_disciplines) == len_before - 1
        assert deleted_discipline not in repo.all_disciplines
        
    def test_delete_discipline_usecase_not_found(self):
        repo = DisciplineRepositoryMock()
        usecase = DeleteDisciplineUsecase(repo)
        discipline_id = 'invalid_id'

        with pytest.raises(HTTPException) as exc:
            usecase(discipline_id)
        
        assert exc.value.status_code == 404
        assert exc.value.detail == 'Discipline not found'