import abc
from typing import List
from src.shared.domain.entities.answer import Answer
from src.shared.domain.entities.schedule import Schedule


class IAnswerRepository:
  
  @abc.abstractmethod
  def get_answers(self) -> List[Answer]:
    pass

  @abc.abstractmethod
  def get_schedule(self) -> Schedule:
    pass
  
  @abc.abstractmethod
  def update_schedule(self, new_url: str) -> Schedule:
    pass
