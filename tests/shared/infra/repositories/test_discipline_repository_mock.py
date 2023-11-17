import copy
from src.shared.domain.entities.discipline import Discipline
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock


class Test_DisciplineRepositoryMock:
    def test_create_discipline(self):
        repo = DisciplineRepositoryMock()
        len_before = len(repo.all_disciplines)
        discipline = Discipline(dicipline_id="aaa-aaa-aaa-aaa", name="Calculo 1", year=2, students_emails_list=[])
        
        new_discipline = repo.create_discipline(discipline)
        
        assert new_discipline == discipline
        assert len(repo.all_disciplines) == len_before + 1
        assert repo.all_disciplines[-1] == discipline
        
    def test_get_discipline_by_id(self):
        repo = DisciplineRepositoryMock()
        
        discipline = repo.get_discipline_by_id("aaa-aaa-ccc-ddd")
        
        assert discipline == repo.all_disciplines[1]
        
    def test_update_discipline_by_id(self):
        repo = DisciplineRepositoryMock()
        
        discipline = copy.deepcopy(repo.get_discipline_by_id("aaa-aaa-ccc-ddd"))
        
        repo.update_discipline_by_id(discipline_id="aaa-aaa-ccc-ddd", new_name="Calculo 2")
        
        new_discipline = repo.get_discipline_by_id("aaa-aaa-ccc-ddd")
        
        assert new_discipline != discipline
        assert new_discipline.name == "Calculo 2"
        assert repo.all_disciplines[1].name == "Calculo 2"
        
    def test_delete_discipline(self):
        repo = DisciplineRepositoryMock()
        len_before = len(repo.all_disciplines)
        
        discipline = repo.delete_discipline("aaa-aaa-ccc-ddd")
        
        assert len(repo.all_disciplines) == len_before - 1
        
    def test_batch_create_disciplines(self):
        repo = DisciplineRepositoryMock()
        len_before = len(repo.all_disciplines)
        disciplines = [
            Discipline("Calculo 1", "aaa-bbb-ccc-ddd", 2, []),
            Discipline("Fisica", "aaa-aaa-ccc-ddd", 2, []),
            Discipline("Automatos", "aaa-ccc-ccc-ddd", 2, []),
        ]
        
        new_disciplines = repo.batch_create_disciplines(disciplines)