from src.modules.get_discipline.app.get_discipline_viewmodel import GetDisciplineViewmodel
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock


class Test_GetDisciplineViewmodel:
    def test_get_discipline_viewmodel(self):
        repo = DisciplineRepositoryMock()
        discipline = repo.all_disciplines[0]
        viewmodel = GetDisciplineViewmodel(discipline).to_dict()
        
        expected = {'discipline': {'name': 'Calculo 1', 'discipline_id': 'aaa-bbb-ccc-ddd', 'year': 2, 'students_emails_list': ['umemail@gmail.com']}, 'message': 'Discipline retrieved successfully'}
        assert viewmodel == expected
        assert viewmodel['discipline']['name'] == repo.all_disciplines[0].name