from src.modules.get_all_disciplines.app.get_all_disciplines_viewmodel import GetAllDisciplinesViewmodel
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock


class Test_GetAllDisciplinesViewmodel:
    def test_get_all_disciplines_viewmodel(self):
        repo = DisciplineRepositoryMock()
        disciplines = repo.get_all_disciplines()
        viewmodel = GetAllDisciplinesViewmodel(disciplines).to_dict()
        assert len(viewmodel["disciplines"]) == len(disciplines)
        assert viewmodel["message"] == "Disciplines found successfully"