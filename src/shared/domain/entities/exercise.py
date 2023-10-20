import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Exercise:
    _exercise_id: str
    _discipline_id: str
    _title: str
    _enunciado: str
    _creation_date: datetime
    _expiration_date: datetime
    _correct_answer: str

    def __init__(self, exercise_id: str, discipline_id, title, enunciado, creation_date, exipiration_date, correct_answer):
        self._exercise_id = exercise_id
        self._discipline_id = discipline_id
        self._title = title
        self._enunciado = enunciado
        self._creation_date = creation_date
        self._expiration_date = exipiration_date
        self._correct_answer = correct_answer


    @property
    def exercise_id(self):
        return self._exercise_id

    @exercise_id.setter
    def exercise_id(self, value):
        if value is None:
            return
        self.exercise_id = value

    @property
    def discipline_id(self):
        return self._exercise_id

    @discipline_id.setter
    def discipline_id(self, value):
        if value is None:
            return
        self.discipline_id = value

    @property
    def title(self):
        return self._exercise_id

    @title.setter
    def title(self, value):
        if value is None:
            return
        self.discipline_id = value


    @property
    def enunciado(self):
        return self._exercise_id

    @enunciado.setter
    def enunciado(self, value):
        if value is None:
            return
        self._enunciado = value


    @property
    def creation_date(self):
        return self._exercise_id

    @creation_date.setter
    def creation_date(self, value):
        if value is None:
            return
        self._creation_date = value











