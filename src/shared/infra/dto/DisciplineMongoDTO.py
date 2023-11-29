from ast import List
from src.shared.domain.entities.discipline import Discipline


class DisciplineMongoDTO:
  name: str
  year: int
  students_emails_list: List[str]
  
  def __init__(self, name, year, students_emails_list):
      self.name = name
      self.year = year
      self.students_emails_list = students_emails_list

  @staticmethod
  def from_entity(discipline: Discipline) -> 'DisciplineMongoDTO':
      return DisciplineMongoDTO(discipline.name, discipline.year, discipline.students_emails_list)
  
  def to_mongo(self) -> dict:
      return {
          'name': self.name,
          'year': self.year,
          'students_emails_list': self.students_emails_list
      }
  
  @staticmethod
  def from_mongo(answer: dict) -> 'DisciplineMongoDTO':
      return DisciplineMongoDTO(answer['name'], answer['year'], answer['students_emails_list'])
  
  def to_entity(self) -> Discipline:
      return Discipline(self.name, self.year, self.students_emails_list)
  
  def __repr__(self):
      return f"DisciplineMongoDTO(name={self.name}, year={self.year}, students_emails_list={self.students_emails_list})"
  
  def __eq__(self, other):
      if not isinstance(other, DisciplineMongoDTO):
          return False
      return self.name == other.name and self.year == other.year and self.students_emails_list == other.students_emails_list