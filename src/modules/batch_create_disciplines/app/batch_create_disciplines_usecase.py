from typing import List
from src.shared.domain.entities.discipline import Discipline
from src.shared.domain.repositories.discipline_respository_interface import IDisciplineRespository
from fastapi import HTTPException, status

class BatchCreateDisciplinesUseCase:
    def __init__(self, repo: IDisciplineRespository):
        self.repo = repo

    def __call__(self, disciplines: List[Discipline]):
        new_ids = []
        for discipline in disciplines:
            if self.repo.get_discipline_by_id(discipline.discipline_id):
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Discipline {discipline.discipline_id} already exists")
            if discipline.discipline_id in new_ids:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Duplicate discipline id {discipline.discipline_id}")
            new_ids.append(discipline.discipline_id)
            
        
        return self.repo.batch_create_disciplines(disciplines)