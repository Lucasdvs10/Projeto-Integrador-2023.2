from src.shared.domain.repositories.discipline_repository_interface import IDisciplineRepository
from fastapi import HTTPException, status

class GetAllDisciplinesUseCase:
    def __init__(self, repo: IDisciplineRepository):
        self.repo = repo
        
    def __call__(self):
        disciplines = self.repo.get_all_disciplines()
        
        if not disciplines:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No disciplines found")
        
        return disciplines