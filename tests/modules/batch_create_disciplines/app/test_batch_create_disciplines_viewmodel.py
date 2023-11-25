from src.modules.batch_create_disciplines.app.batch_create_disciplines_viewmodel import BatchCreateDisciplinesViewmodel
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock


class Test_BatchCreateDisciplinesViewmodel:
    def test_batch_create_disciplines_viewmodel(self):
        repo = DisciplineRepositoryMock()
        disciplines = [repo.all_disciplines[0], repo.all_disciplines[1], repo.all_disciplines[2]]
        viewmodel = BatchCreateDisciplinesViewmodel(disciplines).to_dict()
        
        expected = {'disciplines': [{'name': 'Calculo 1', 'discipline_id': 'aaa-bbb-ccc-ddd', 'year': 2, 'students_emails_list': ['umemail@gmail.com']}, {'name': 'Fisica', 'discipline_id': 'aaa-aaa-ccc-ddd', 'year': 2, 'students_emails_list': ['outro@gmail.com']}, {'name': 'Automatos', 'discipline_id': 'aaa-ccc-ccc-ddd', 'year': 2, 'students_emails_list': ['maisum@gmail.com']}], 'message': 'Disciplines created successfully'}
        
        assert viewmodel == expected