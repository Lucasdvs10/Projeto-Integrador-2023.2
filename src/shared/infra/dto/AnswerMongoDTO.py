from src.shared.domain.entities.answer import Answer


class AnswerMongoDTO:
    answer_id: str
    exercise_id: str
    email: str
    content: str
    is_right: 0 | 1
    
    def __init__(self, answer_id, exercise_id, email, content, is_right):
        self.answer_id = answer_id
        self.exercise_id = exercise_id
        self.email = email
        self.content = content
        self.is_right = is_right
        
        
    @staticmethod
    def from_entity(answer: Answer) -> 'AnswerMongoDTO':
        return AnswerMongoDTO(answer.answer_id, answer.exercise_id, answer.email, answer.content, answer.is_right)
    
    def to_mongo(self) -> dict:
        return {
            'answer_id': self.answer_id,
            'exercise_id': self.exercise_id,
            'email': self.email,
            'content': self.content,
            'is_right': self.is_right
        }
    
    @staticmethod
    def from_mongo(answer: dict) -> 'AnswerMongoDTO':
        return AnswerMongoDTO(answer['answer_id'], answer['exercise_id'], answer['email'], answer['content'], answer['is_right'])
    
    def to_entity(self) -> Answer:
        return Answer(self.answer_id, self.exercise_id, self.email, self.content, self.is_right)
    
    def __repr__(self):
        return f"AnswerMongoDTO(answer_id={self.answer_id}, exercise_id={self.exercise_id}, email={self.email}, content={self.content}, is_right={self.is_right})"
    
    def __eq__(self, other):
        if not isinstance(other, AnswerMongoDTO):
            return False
        return self.answer_id == other.answer_id and self.exercise_id == other.exercise_id and self.email == other.email and self.content == other.content and self.is_right == other.is_right