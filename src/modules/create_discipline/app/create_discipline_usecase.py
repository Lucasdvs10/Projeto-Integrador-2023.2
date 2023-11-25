from src.shared.domain.entities.discipline import Discipline
from src.shared.domain.repositories.discipline_repository_interface import IDisciplineRepository
import uuid

class CreateDisciplineUsecase:
    def __init__(self, repo: IDisciplineRepository):
        self.repo = repo
        
    def __call__(self, name: str, year: int, students_emails_list: str = []):
        discipline_id = str(uuid.uuid4())
        while self.repo.get_discipline_by_id(discipline_id) is not None:
            discipline_id = str(uuid.uuid4())
            
        new_discipline = Discipline(discipline_id=discipline_id, name=name, year=year, students_emails_list=students_emails_list)
        discipline = self.repo.create_discipline(new_discipline)
        return discipline