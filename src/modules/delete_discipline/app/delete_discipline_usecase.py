from src.shared.domain.repositories.discipline_repository_interface import IDisciplineRepository
from fastapi import HTTPException, status

class DeleteDisciplineUsecase:
    def __init__(self, repo: IDisciplineRepository):
        self.repo = repo
        
    def __call__(self, discipline_id: str):
        discipline = self.repo.get_discipline_by_id(discipline_id)
        if not discipline:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Discipline not found")
        
        return self.repo.delete_discipline(discipline_id)