from src.modules.create_discipline.app.create_discipline_usecase import CreateDisciplineUsecase
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock


class Test_CreateDisciplineUsecase:
    def test_should_create_discipline(self):
        repo = DisciplineRepositoryMock()
        usecase = CreateDisciplineUsecase(repo)
        len_before = len(repo.all_disciplines)
        discipline = usecase(name="Disciplina 1", year=1, students_emails_list=["22.01102-0@maua.br"])
        assert discipline is not None
        assert discipline.name == "Disciplina 1"
        assert discipline.year == 1
        assert repo.get_discipline_by_id(discipline.discipline_id) is not None
        assert len(repo.all_disciplines) == len_before + 1
        
    def test_should_create_discipline_without_students(self):
        repo = DisciplineRepositoryMock()
        usecase = CreateDisciplineUsecase(repo)
        len_before = len(repo.all_disciplines)
        discipline = usecase(name="Disciplina 1", year=1)
        assert discipline is not None
        assert discipline.name == "Disciplina 1"
        assert discipline.year == 1
        assert discipline.students_emails_list == []
        assert repo.get_discipline_by_id(discipline.discipline_id) is not None
        assert len(repo.all_disciplines) == len_before + 1