from typing import List
from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.repositories.answer_repository_interface import IAnswerRepository
from src.shared.domain.entities.answer import Answer

class AnswerRepositoryMock(IAnswerRepository):
  def __init__(self):
    self.all_answers = [
      Answer("A resposta vem aqui!", "umemail@gmail.com", "content", 0),
      Answer("A resposta do ex1 é essa", "outro@gmail.com", "content", 1),
      Answer("A resposta do ex2 é essa", "maisum@gmail.com", "content", 0),
      Answer("A resposta do ex3 é essa", "olhaoutroaqui@gmail.com", "content", 1),
      Answer("A resposta do ex4 é essa", "meudeusquantoemail@gmail.com", "content", 0),
      Answer("A resposta do ex5 é essa", "minhacriatividadeacabou@gmail.com", "content", 1),
    ]
    
    self.schedule = Schedule("https://www.google.com")
    
  def get_answers(self) -> List[Answer]:
    return self.all_answers
  
  def get_schedule(self) -> Schedule:
    return self.schedule
  
  def update_schedule(self, new_url: str) -> Schedule:
    self.schedule = Schedule(new_url)
    return self.schedule
    
  
  