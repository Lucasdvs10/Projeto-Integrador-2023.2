from typing import List, Optional
from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.repositories.answer_repository_interface import IAnswerRepository
from src.shared.domain.entities.answer import Answer
from src.shared.domain.entities.exercise import Exercise

class AnswerRepositoryMock(IAnswerRepository):
  def __init__(self):
    self.all_answers = [
      Answer("0", "111-111-111", "22.01049-0@maua.br", "A resposta vem aqui!", 0),
      Answer("1", "111-111-111", "outro@gmail.com", "content", 1),
      Answer("2", "111-111-111", "maisum@gmail.com", "content", 0),
      Answer("3", "111-111-111", "olhaoutroaqui@gmail.com", "content", 1),
      Answer("4", "111-222-111", "meudeusquantoemail@gmail.com", "content", 0),
      Answer("5", "111-222-111", "minhacriatividadeacabou@gmail.com", "content", 1),
      Answer("6", "111-222-111", "minhacriatividadeacabou2@gmail.com", "content", 1),
      Answer("7", "111-222-111", "minhacriatividadeacabou3@gmail.com", "content", 1),
    ]
    
    self.all_exercises = [
      Exercise(exercise_id="111-111-111",
               title="Primeiro Presidente do Brasil",
               enunciado="Quem foi o primeiro presidente do Brasil?",
               creation_date=1673319600000,
               expiration_date=1676084400000,
               correct_answer="Marechal Deodoro"
               ),
      Exercise(exercise_id="111-222-111",
               title="Qual lingua é mais antiga",
               enunciado="Qual lingua é mais antiga: Python ou java",
               creation_date=1673319600000,
               expiration_date=1676084400000,
               correct_answer="Python"
               )
    ]
    
        
    self.schedule = Schedule("https://www.google.com")
    
  def get_answers(self, exercise_id) -> List[Answer]:
    return [answer for answer in self.all_answers if answer.exercise_id == exercise_id]
  
  def create_answer(self, answer: Answer) -> Answer:
    self.all_answers.append(answer)
    return answer
  
  def get_answer(self, answer_id: str) -> Answer:
    for answer in self.all_answers:
      if (answer.answer_id == answer_id):
        return answer
    return None
  
  def update_answer(self, answer_id: str, new_content: Optional[str] = None, new_email: Optional[str] = None, new_is_right: Optional[int] = None) -> Answer:
    answer = self.get_answer(answer_id)
    if new_content is not None:
      answer.content = new_content
    if new_email is not None:
      answer.email = new_email
    if new_is_right is not None:
      answer.is_right = new_is_right
    return answer
  
  def delete_answer(self, answer_id: str) -> Answer:
    for answer in self.all_answers:
      if (answer.answer_id == answer_id):
        self.all_answers.remove(answer)
        return answer
      
  def get_schedule(self) -> Schedule:
    return self.schedule
  
  def update_schedule(self, new_url: str) -> Schedule:
    self.schedule = Schedule(new_url)
    return self.schedule
    
  
  