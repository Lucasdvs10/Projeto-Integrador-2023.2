from src.modules.update_discipline.app.update_discipline_viewmodel import UpdateDisciplineViewmodel
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock


class Test_UpdateDisciplineViewmodel:
    def test_update_discipline_viewmodel(self):
        repo = DisciplineRepositoryMock()
        discipline = repo.all_disciplines[0]
        viewmodel = UpdateDisciplineViewmodel(discipline).to_dict()
        
        expected = {'discipline': {'name': 'Calculo 1', 'discipline_id': 'aaa-bbb-ccc-ddd', 'year': 2, 'students_emails_list': ['umemail@gmail.com']}, 'message': 'Discipline updated successfully'}
        assert viewmodel == expected
        assert viewmodel['discipline']['name'] == repo.all_disciplines[0].name