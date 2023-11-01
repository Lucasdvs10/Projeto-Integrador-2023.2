import abc
from typing import List
from src.shared.domain.entities.answer import Answer


class IAnswerRepository:
  
  @abc.abstractmethod
  def get_answers(self) -> List[Answer]:
    pass
