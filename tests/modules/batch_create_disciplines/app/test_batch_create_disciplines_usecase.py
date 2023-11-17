from fastapi.exceptions import HTTPException
import pytest
from src.modules.batch_create_disciplines.app.batch_create_disciplines_usecase import BatchCreateDisciplinesUseCase
from src.shared.domain.entities.discipline import Discipline
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock
import random

class Test_BatchCreateDisciplinesUseCase:
    def test_batch_create_disciplines_usecase(self):
        repo = DisciplineRepositoryMock()
        usecase = BatchCreateDisciplinesUseCase(repo)
        len_before = len(repo.all_disciplines)
        random_ids = [f"{random.choice(['aaa', 'bbb', 'ccc', 'ddd'])}-{random.choice(['aaa', 'bbb', 'ccc', 'ddd'])}-{random.choice(['aaa', 'bbb', 'ccc', 'ddd'])}-{random.choice(['aaa', 'bbb', 'ccc', 'ddd'])}" for _ in range(5)]
        new_disciplines = [Discipline(name="Calculo 4", discipline_id=random_ids[0], year=2, students_emails_list=[]),
                           Discipline(name="Fisica 7", discipline_id=random_ids[1], year=2, students_emails_list=[]),
                           Discipline(name="Digao", discipline_id=random_ids[2], year=2, students_emails_list=[])]
        
        new_disciplines = usecase(new_disciplines)
        
        assert len(repo.all_disciplines) == len_before + len(new_disciplines)
        assert repo.all_disciplines[-3:] == new_disciplines
        
    def test_batch_create_disciplines_with_existing_discipline(self):
        repo = DisciplineRepositoryMock()
        usecase = BatchCreateDisciplinesUseCase(repo)
        len_before = len(repo.all_disciplines)
        new_disciplines = [Discipline(name="Calculo 4", discipline_id="aaa-aaa-aaa-aaa", year=2, students_emails_list=[]),
                           Discipline(name="Fisica 7", discipline_id="aaa-aaa-ccc-ddd", year=2, students_emails_list=[]),
                           Discipline(name="Digao", discipline_id="aaa-ccc-ccc-ddd", year=2, students_emails_list=[])]
        
        with pytest.raises(HTTPException) as exc:
            new_disciplines = usecase(new_disciplines)
        assert exc.value.status_code == 409
        assert exc.value.detail == f"Discipline {new_disciplines[1].discipline_id} already exists"
        
    def test_batch_create_disciplines_with_duplicate_discipline(self):
        repo = DisciplineRepositoryMock()
        usecase = BatchCreateDisciplinesUseCase(repo)
        len_before = len(repo.all_disciplines)
        new_disciplines = [Discipline(name="Digao", discipline_id="aer-ial-sin-the-sky", year=2, students_emails_list=[]),
                           Discipline(name="Digao", discipline_id="aer-ial-sin-the-sky", year=2, students_emails_list=[])]
        
        with pytest.raises(HTTPException) as exc:
            new_disciplines = usecase(new_disciplines)
        assert exc.value.status_code == 409
        assert exc.value.detail == f"Duplicate discipline id {new_disciplines[-1].discipline_id}"