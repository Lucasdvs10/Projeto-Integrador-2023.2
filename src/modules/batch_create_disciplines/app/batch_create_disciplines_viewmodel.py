from typing import List

from src.shared.domain.entities.discipline import Discipline


class DisciplineViewmodel:
    name: str
    discipline_id: str
    year: int
    students_emails_list: List[str]
    
    def __init__(self, discipline):
        self.name = discipline.name
        self.discipline_id = discipline.discipline_id
        self.year = discipline.year
        self.students_emails_list = discipline.students_emails_list
        
    def to_dict(self):
        return {
            "name": self.name,
            "discipline_id": self.discipline_id,
            "year": self.year,
            "students_emails_list": self.students_emails_list
        }
        
class BatchCreateDisciplinesViewmodel:
    disciplines: List[DisciplineViewmodel]
    
    def __init__(self, disciplines: List[Discipline]):
        self.disciplines = [DisciplineViewmodel(discipline) for discipline in disciplines]
        
    def to_dict(self):
        return {
            "disciplines": [discipline.to_dict() for discipline in self.disciplines],
            "message": "Disciplines created successfully"
        }