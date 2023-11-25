from src.shared.domain.repositories.discipline_repository_interface import IDisciplineRepository
from fastapi import HTTPException, status

class UpdateDisciplineUsecase:
    def __init__(self, repo: IDisciplineRepository):
        self.repo = repo
        
    def __call__(self, discipline_id: str, new_name: str = None, new_year: int = None, new_students_list: str = None):
        if not self.repo.get_discipline_by_id(discipline_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Discipline not found")
        
        updated_discipline = self.repo.update_discipline_by_id(discipline_id, new_name, new_year, new_students_list)
        
        return updated_discipline