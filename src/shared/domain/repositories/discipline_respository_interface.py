import abc
from typing import List, Optional

from src.shared.domain.entities.discipline import Discipline


class IDisciplineRepository:

    @abc.abstractmethod
    def create_discipline(self, new_discipline: Discipline) -> Discipline:
        pass

    @abc.abstractmethod
    def get_discipline_by_id(self, discipline_id: str) -> Optional[Discipline]:
        pass

    @abc.abstractmethod
    def update_discipline_by_id(self, discipline_id: str, new_name: Optional[str], new_year: Optional[int], new_students_list: Optional[str]) -> Optional[Discipline]:
        pass

    @abc.abstractmethod
    def delete_discipline(self, discipline_id) -> Optional[Discipline]:
        pass
    
    @abc.abstractmethod
    def batch_create_disciplines(self, disciplines: List[Discipline]) -> List[Discipline]:
        pass
    
    @abc.abstractmethod
    def get_all_disciplines(self) -> List[Discipline]:
        pass