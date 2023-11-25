from src.modules.delete_discipline.app.delete_discipline_viewmodel import DeleteDisciplineViewmodel
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock


class Test_DeleteDisciplineViewmodel:
    def test_delete_discipline_viewmodel(self):
        repo = DisciplineRepositoryMock()
        discipline = repo.all_disciplines[0]
        viewmodel = DeleteDisciplineViewmodel(discipline).to_dict()
        
        expected = {'discipline': {'name': 'Calculo 1', 'discipline_id': 'aaa-bbb-ccc-ddd', 'year': 2, 'students_emails_list': ['umemail@gmail.com']}, 'message': 'Discipline deleted successfully'}
        assert viewmodel == expected
        assert viewmodel['discipline']['name'] == repo.all_disciplines[0].name