from src.shared.domain.entities.discipline import Discipline
from src.shared.infra.repositories.discipline_repository_mock import DisciplineRepositoryMock
from src.shared.infra.repositories.discipline_repository_mongo import DisciplineRepositoryMongo
import pytest

class Test_DisciplineRepositoryMongo:
    def test_batch_create_disciplines(self):
        repo_mongo = DisciplineRepositoryMongo()
        repo_mock = DisciplineRepositoryMock()
        len_before = len(repo_mongo.get_all_disciplines())
        disciplines = repo_mock.get_all_disciplines()
        
        resp = repo_mongo.batch_create_disciplines(disciplines)
        assert resp == disciplines
        assert len(repo_mongo.get_all_disciplines()) == len_before + len(disciplines)
        
    def test_create_discipline(self):
        repo_mongo = DisciplineRepositoryMongo()
        len_before = len(repo_mongo.get_all_disciplines())
        discipline = Discipline(name="Teste", discipline_id="123", year=2021, students_emails_list=[])
        
        resp = repo_mongo.create_discipline(discipline)
        assert resp == discipline
        assert len(repo_mongo.get_all_disciplines()) == len_before + 1
        
    def test_get_discipline_by_id(self):
        repo_mongo = DisciplineRepositoryMongo()
        resp = repo_mongo.get_discipline_by_id("123")
        assert resp == Discipline(name="Teste", discipline_id="123", year=2021, students_emails_list=[])
        
    def test_update_discipline_by_id(self):
        repo_mongo = DisciplineRepositoryMongo()
        resp = repo_mongo.update_discipline_by_id("123", new_name="Teste2")
        assert resp == Discipline(name="Teste2", discipline_id="123", year=2021, students_emails_list=[])
        
    def test_delete_discipline(self):
        repo_mongo = DisciplineRepositoryMongo()
        len_before = len(repo_mongo.get_all_disciplines())
        resp = repo_mongo.delete_discipline("123")
        assert resp == Discipline(name="Teste2", discipline_id="123", year=2021, students_emails_list=[])
        assert len(repo_mongo.get_all_disciplines()) == len_before - 1
        
    def test_get_all_disciplines(self):
        repo_mongo = DisciplineRepositoryMongo()
        resp = repo_mongo.get_all_disciplines()
        assert all([isinstance(discipline, Discipline) for discipline in resp])