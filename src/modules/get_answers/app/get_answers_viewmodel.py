from typing import List

from src.shared.domain.entities.answer import Answer


class AnswerViewmodel:
  exercise_id: str
  email: str
  content: str
  is_right: 0 | 1
  
  def __init__(self, answer: Answer):
    self.exercise_id = answer.exercise_id
    self.email = answer.email
    self.content = answer.content
    self.is_right = answer.is_right
    
  def to_dict(self):
    return {
      "exercise_id": self.exercise_id,
      "email": self.email,
      "content": self.content,
      "is_right": self.is_right
    }
    
class GetAnswersViewmodel:
  answers: List[AnswerViewmodel]
  def __init__(self, answers: List[Answer]):
    self.answers = [AnswerViewmodel(answer) for answer in answers]
    
  def to_dict(self):
    return {
      "answers": [answer.to_dict() for answer in self.answers],
      "message": "Answers retrieved successfully"
    }