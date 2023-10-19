import abc
from typing import Optional

from src.shared.domain.entities.discipline import Discipline


class IDisciplineRespository:

    @abc.abstractmethod
    def create_discipline(self, new_discipline: Discipline) -> Discipline:
        pass

    @abc.abstractmethod
    def get_discipline_by_id(self, discipline_id: str) -> Discipline:
        pass

    @abc.abstractmethod
    def update_discipline_by_id(self, discipline_id: str, new_name: Optional[str], new_year: Optional[int], new_students_list: Optional[str]) -> Discipline:
        pass

    @abc.abstractmethod
    def delete_discipline(self, discipline_id) -> Discipline:
        pass
