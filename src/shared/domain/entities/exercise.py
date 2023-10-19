import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Exercise:
    _exercise_id: str
    _discipline_id: str
    _title: str
    _enunciado: str
    _creation_date: datetime
    _expiration_date: dataclasses
    _correct_answer: str

    def __init__(self, exercise_id: str, discipline_id, title, enunciado, creation_date, exipiration_date, correct_answer):
        self._exercise_id = exercise_id
        self._discipline_id = discipline_id
        self._title = title
        self._enunciado = enunciado
        self._creation_date = creation_date
        self._expiration_date = exipiration_date
        self._correct_answer = correct_answer
