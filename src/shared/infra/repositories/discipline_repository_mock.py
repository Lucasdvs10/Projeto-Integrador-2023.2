from typing import List, Optional

from src.shared.domain.entities.discipline import Discipline
from src.shared.domain.repositories.discipline_respository_interface import IDisciplineRespository


class DisciplineRepositoryMock(IDisciplineRespository):

    def __init__(self):
        self.all_disciplines = [
            Discipline("Calculo 1", "aaa-bbb-ccc-ddd", 2, ["umemail@gmail.com"]),
            Discipline("Fisica", "aaa-aaa-ccc-ddd", 2, ["outro@gmail.com"]),
            Discipline("Automatos", "aaa-ccc-ccc-ddd", 2, ["maisum@gmail.com"]),
            Discipline("Java", "aaa-ddd-ccc-ddd", 1, ["olhaoutroaqui@gmail.com"]),
            Discipline("Banco de dados", "aaa-eee-ccc-ddd", 1, ["meudeusquantoemail@gmail.com"]),
            Discipline("Front end", "aaa-fff-ccc-ddd", 1, ["minhacriatividadeacabou@gmail.com"]),
        ]

    def create_discipline(self, new_discipline: Discipline) -> Discipline:
        self.all_disciplines.append(new_discipline)
        return new_discipline

    def get_discipline_by_id(self, discipline_id: str) -> Optional[Discipline]:
        for discipline in self.all_disciplines:
            if discipline.discipline_id == discipline_id:
                return discipline
        return None

    def update_discipline_by_id(self, discipline_id: str, new_name: Optional[str] = None, new_year: Optional[int] = None,
                                new_students_list: Optional[str] = None) -> Optional[Discipline]:

        discipline_to_update = self.get_discipline_by_id(discipline_id)
        if discipline_to_update is None:
            return None
        if new_name:
            discipline_to_update.name = new_name
        if new_year:
            discipline_to_update.year = new_year
        if new_students_list:
            discipline_to_update.students_emails_list = new_students_list
            
        return discipline_to_update

    def delete_discipline(self, discipline_id) -> Optional[Discipline]:
        for discipline in self.all_disciplines:
            if discipline.discipline_id == discipline_id:
                self.all_disciplines.remove(discipline)
                return discipline
        return None

    def batch_create_disciplines(self, disciplines: List[Discipline]) -> List[Discipline]:
        for discipline in disciplines:
            self.all_disciplines.append(discipline)
        return disciplines
    
    def get_all_disciplines(self) -> List[Discipline]:
        return self.all_disciplines