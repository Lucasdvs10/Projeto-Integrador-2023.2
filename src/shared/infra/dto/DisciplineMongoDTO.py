from typing import List
from src.shared.domain.entities.discipline import Discipline


class DisciplineMongoDTO:
    name: str
    discipline_id: str
    year: int
    students_emails_list: List[str]
  
    def __init__(self, name, discipline_id, year, students_emails_list):
        self.name = name
        self.discipline_id = discipline_id
        self.year = year
        self.students_emails_list = students_emails_list

    @staticmethod
    def from_entity(discipline: Discipline) -> 'DisciplineMongoDTO':
        return DisciplineMongoDTO(discipline.name, discipline.discipline_id, discipline.year, discipline.students_emails_list)

    def to_mongo(self) -> dict:
        return {
            'discipline_id': self.discipline_id,
            'name': self.name,
            'year': self.year,
            'students_emails_list': self.students_emails_list
        }

    @staticmethod
    def from_mongo(answer: dict) -> 'DisciplineMongoDTO':
        return DisciplineMongoDTO(answer['name'], answer['discipline_id'], answer['year'], answer['students_emails_list'])

    def to_entity(self) -> Discipline:
        return Discipline(self.name, self.discipline_id, self.year, self.students_emails_list)

    def __repr__(self):
        return f"DisciplineMongoDTO(name={self.name}, discipline_id={self.discipline_id}, year={self.year}, students_emails_list={self.students_emails_list})"

    def __eq__(self, other):
        if not isinstance(other, DisciplineMongoDTO):
            return False
        return self.name == other.name and self.discipline_id == other.discipline_id and self.year == other.year and self.students_emails_list == other.students_emails_list