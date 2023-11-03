import dataclasses

from src.shared.helpers.errors.domain_errors import EntityParameterError

@dataclasses.dataclass
class Exercise:
    _exercise_id: str
    _title: str
    _enunciado: str
    _creation_date: int # milliseconds
    _expiration_date: int # milliseconds
    _correct_answer: str
    MIN_TITLE_LENGTH = 3
    MAX_TITLE_LENGTH = 150
    MIN_ENUNCIADO_LENGTH = 3
    MAX_ENUNCIADO_LENGTH = 500

    def __init__(self, exercise_id: str, title: str, enunciado: str, creation_date: int, expiration_date: int, correct_answer: str):
        if exercise_id is None:
            raise EntityParameterError("Exercise id must be provided")
        if type(exercise_id) is not str:
            raise EntityParameterError("Exercise id must be a string")
        self._exercise_id = exercise_id
        
        if title is None:
            raise EntityParameterError("Title must be provided")
        if type(title) is not str:
            raise EntityParameterError("Title must be a string")
        if len(title) < self.MIN_TITLE_LENGTH:
            raise EntityParameterError(f"Title must have at least {self.MIN_TITLE_LENGTH} characters")
        if len(title) > self.MAX_TITLE_LENGTH:
            raise EntityParameterError(f"Title must have at most {self.MAX_TITLE_LENGTH} characters")
        self._title = title
        
        if enunciado is None:
            raise EntityParameterError("Enunciado must be provided")
        if type(enunciado) is not str:
            raise EntityParameterError("Enunciado must be a string")
        if len(enunciado) < self.MIN_ENUNCIADO_LENGTH:
            raise EntityParameterError(f"Enunciado must have at least {self.MIN_ENUNCIADO_LENGTH} characters")
        if len(enunciado) > self.MAX_ENUNCIADO_LENGTH:
            raise EntityParameterError(f"Enunciado must have at most {self.MAX_ENUNCIADO_LENGTH} characters")
        self._enunciado = enunciado
        
        if creation_date is None:
            raise EntityParameterError("Creation date must be provided")
        if type(creation_date) is not int:
            raise EntityParameterError("Creation date must be a int")
        if not 1577847600000 <= creation_date <= 3387133800000:
            raise EntityParameterError("Creation date must be between 2020-01-01 and 2077-05-01")
        self._creation_date = creation_date
        
        if expiration_date is None:
            raise EntityParameterError("Expiration date must be provided")
        if type(expiration_date) is not int:
            raise EntityParameterError("Expiration date must be a int")
        if not 1577847600000 <= expiration_date <= 3387133800000:
            raise EntityParameterError("Expiration date must be between 2020-01-01 and 2077-05-01")

        if(expiration_date <= creation_date):
            raise EntityParameterError("Expiration date must be after creation date")

        self._expiration_date = expiration_date
        
        if correct_answer is None:
            raise EntityParameterError("Correct answer must be provided")
        if type(correct_answer) is not str:
            raise EntityParameterError("Correct answer must be a string")
        self._correct_answer = correct_answer


    @property
    def exercise_id(self):
        return self._exercise_id

    @exercise_id.setter
    def exercise_id(self, value):
        if value is None:
            raise EntityParameterError("Exercise id must be provided")
        self._exercise_id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value is None:
            raise EntityParameterError("Title must be provided")
        self._title = value


    @property
    def enunciado(self):
        return self._enunciado

    @enunciado.setter
    def enunciado(self, value):
        if value is None:
            raise EntityParameterError("Enunciado must be provided")
        self._enunciado = value


    @property
    def creation_date(self):
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        if value is None:
            raise EntityParameterError("Creation date must be provided")
        self._creation_date = value


    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        if value is None:
            raise EntityParameterError("Expiration date must be provided")
        self._expiration_date = value

    @property
    def correct_answer(self):
        return self._correct_answer

    @correct_answer.setter
    def correct_answer(self, value):
        if value is None:
            raise EntityParameterError("Correct answer must be provided")
        self._correct_answer = value


