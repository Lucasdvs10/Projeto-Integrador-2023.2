import abc
from typing import List, Optional
from src.shared.domain.entities.answer import Answer
from src.shared.domain.entities.schedule import Schedule


class IAnswerRepository:
  
  @abc.abstractmethod
  def get_answers(self, exercise_id) -> List[Answer]:
    pass
  
  @abc.abstractmethod
  def create_answer(self, answer: Answer) -> Answer:
    pass
  
  @abc.abstractmethod
  def get_answer(self, answer_id: str) -> Answer:
    pass
  
  @abc.abstractmethod
  def update_answer(self, answer_id: str, new_content: Optional[str], new_email: Optional[str], new_is_right: Optional[int]) -> Answer:
    pass
  
  @abc.abstractmethod
  def delete_answer(self, answer_id: str) -> Answer:
    pass

  @abc.abstractmethod
  def get_schedule(self) -> Schedule:
    pass
  
  @abc.abstractmethod
  def update_schedule(self, new_url: str) -> Schedule:
    pass
