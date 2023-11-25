from src.modules.create_discipline.app.create_discipline_viewmodel import CreateDisciplineViewmodel
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock


class Test_CreateDisciplineViewmodel:
    def test_create_discipline_viewmodel(self):
        repo = DisciplineRepositoryMock()
        discipline = repo.all_disciplines[0]
        viewmodel = CreateDisciplineViewmodel(discipline).to_dict()
        
        expected = {'discipline': {'name': 'Calculo 1', 'discipline_id': 'aaa-bbb-ccc-ddd', 'year': 2, 'students_emails_list': ['umemail@gmail.com']}, 'message': 'Discipline created successfully'}
        assert viewmodel == expected
        assert viewmodel['discipline']['name'] == repo.all_disciplines[0].name