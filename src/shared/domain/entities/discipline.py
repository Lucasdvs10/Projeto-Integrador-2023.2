import dataclasses
from typing import List

from src.shared.helpers.errors.domain_errors import EntityParameterTypeError


@dataclasses.dataclass
class Discipline:
    _name: str
    _discipline_id: str
    _year: int
    _students_emails_list: List[str]

    def __init__(self, name, dicipline_id, year, students_emails_list):
        if type(name) != str:
            raise EntityParameterTypeError("Name")
        self._name = name

        if type(dicipline_id) != str:
            raise EntityParameterTypeError("Discipline ID")
        self._discipline_id = dicipline_id

        if type(year) != int:
            raise EntityParameterTypeError("year")
        self._year = year

        if type(students_emails_list) != list:
            raise EntityParameterTypeError("students_emails_list")
        self._students_emails_list = students_emails_list

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise EntityParameterTypeError("name")
        self._name = value

    @property
    def discipline_id(self):
        return self._discipline_id

    @discipline_id.setter
    def discipline_id(self, value):
        if type(value) != str:
            raise EntityParameterTypeError("Discipline ID")
        self._discipline_id = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if type(value) != int:
            raise EntityParameterTypeError("year")
        self._year = value

    @property
    def students_emails_list(self):
        return self._students_emails_list

    @students_emails_list.setter
    def students_emails_list(self, value):
        if type(value) != list:
            raise EntityParameterTypeError("students_emails_list")
        self._students_emails_list = value

