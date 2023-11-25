from src.shared.domain.entities.answer import Answer

class AnswerViewmodel:
    answer_id: str
    exercise_id: str
    email: str
    content: str
    is_right: 0 | 1
    
    def __init__(self, answer: Answer):
      self.answer_id = answer.answer_id
      self.exercise_id = answer.exercise_id
      self.email = answer.email
      self.content = answer.content
      self.is_right = answer.is_right
        
    def to_dict(self):
      return {
          "answer_id": self.answer_id,
          "exercise_id": self.exercise_id,
          "email": self.email,
          "content": self.content,
          "is_right": self.is_right,
      }
        
class DeleteAnswerViewmodel:
    answer: AnswerViewmodel
    
    def __init__(self, answer: Answer):
        self.answer = AnswerViewmodel(answer)
        
    def to_dict(self):
        return {
            "answer": self.answer.to_dict(),
            "message": "Answer deleted successfully"
        }