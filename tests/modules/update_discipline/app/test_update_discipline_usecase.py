import pytest
from src.modules.update_discipline.app.update_discipline_usecase import UpdateDisciplineUsecase
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock
import copy
from fastapi import HTTPException

class Test_UpdateDisciplineUsecase:
    def test_update_discipline_usecase(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        discipline_id = repo.all_disciplines[0].discipline_id
        old_discipline = copy.deepcopy(repo.all_disciplines[0])
        
        response = usecase(discipline_id, new_name="Discipline 2", new_students_list=["19.08432-0@maua.br"], new_year=2)
        
        assert response.name == "Discipline 2"
        assert repo.all_disciplines[0] == response
        assert repo.all_disciplines[0] != old_discipline
        
    def test_update_discipline_usecase_with_not_found_id(self):
        repo = DisciplineRepositoryMock()
        usecase = UpdateDisciplineUsecase(repo)
        discipline_id = "not-fou-nd-id"
        
        with pytest.raises(HTTPException) as exc:
            response = usecase(discipline_id, new_name="Discipline 2")
        assert exc.value.status_code == 404
        assert exc.value.detail == "Discipline not found"