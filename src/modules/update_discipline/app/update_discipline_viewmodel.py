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
        
class UpdateDisciplineViewmodel:
    discipline: DisciplineViewmodel
    
    def __init__(self, discipline: Discipline):
        self.discipline = DisciplineViewmodel(discipline)
        
    def to_dict(self):
        return {
            "discipline": self.discipline.to_dict(),
            "message": "Discipline updated successfully"
        }