from src.shared.domain.entities.answer import Answer


class AnswerViewmodel:
    answer_id: str
    exercise_id: str
    content: str
    email: str
    is_right: int
    
    def __init__(self, answer: Answer):
        self.answer_id = answer.answer_id
        self.exercise_id = answer.exercise_id
        self.content = answer.content
        self.email = answer.email
        self.is_right = answer.is_right
        
    def to_dict(self):
        return {
            "answer_id": self.answer_id,
            "exercise_id": self.exercise_id,
            "content": self.content,
            "email": self.email,
            "is_right": self.is_right,
        }
        
class UpdateAnswerViewmodel:
    answer: AnswerViewmodel
    def __init__(self, answer: Answer):
        self.answer = AnswerViewmodel(answer)
        
    def to_dict(self):
        return {
            "answer": self.answer.to_dict(),
            "message": "Answer updated successfully"
        }