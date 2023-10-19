import pytest

from src.shared.domain.entities.discipline import Discipline
from src.shared.helpers.errors.domain_errors import EntityParameterTypeError


class Test_Discipline:
    def test_instantiate_discipline(self):
        discipline = Discipline("Calculo", "aisdjasdjiou", 2023, [])

        assert discipline is not None

    def test_change_discipline_name(self):
        discipline = Discipline("Calculo", "aisdjasdjiou", 2023, [])

        discipline.name = "Outra disciplina"

        assert discipline.name == "Outra disciplina"

    def test_change_discipline_name_to_a_invalid_one(self):
        discipline = Discipline("Calculo", "aisdjasdjiou", 2023, [])

        with(pytest.raises(EntityParameterTypeError)):
            discipline.name = 42

    def test_change_discipline_id(self):
        discipline = Discipline("Calculo", "aisdjasdjiou", 2023, [])

        assert discipline.discipline_id == "aisdjasdjiou"

    def test_change_discipline_id_to_a_invalid_one(self):
        discipline = Discipline("Calculo", "aisdjasdjiou", 2023, [])

        with(pytest.raises(EntityParameterTypeError)):
            discipline.discipline_id = 1996

    def test_change_discipline_year(self):
        discipline = Discipline("Calculo", "aisdjasdjiou", 2023, [])

        assert discipline.year == 2023

    def test_change_discipline_year_to_a_invalid_one(self):
        discipline = Discipline("Calculo", "aisdjasdjiou", 2023, [])

        with(pytest.raises(EntityParameterTypeError)):
            discipline.year = "Uma string"

    def test_change_discipline_students_list(self):
        discipline = Discipline("Calculo", "aisdjasdjiou", 2023, [])

        assert discipline.students_emails_list == []

    def test_change_discipline_students_list_to_a_invalid_one(self):
        discipline = Discipline("Calculo", "aisdjasdjiou", 2023, [])

        with(pytest.raises(EntityParameterTypeError)):
            discipline.students_emails_list = "Uma lista em string"




