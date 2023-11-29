from src.shared.domain.entities.answer import Answer


class AnswerMongoDTO:
    exercise_id: str
    email: str
    content: str
    is_right: 0 | 1
    
    def __init__(self, exercise_id, email, content, is_right):
        self.exercise_id = exercise_id
        self.email = email
        self.content = content
        self.is_right = is_right
        
        
    @staticmethod
    def from_entity(answer: Answer) -> 'AnswerMongoDTO':
        return AnswerMongoDTO(answer.exercise_id, answer.email, answer.content, answer.is_right)
    
    def to_mongo(self) -> dict:
        return {
            'exercise_id': self.exercise_id,
            'email': self.email,
            'content': self.content,
            'is_right': self.is_right
        }
    
    @staticmethod
    def from_mongo(answer: dict) -> 'AnswerMongoDTO':
        return AnswerMongoDTO(answer['exercise_id'], answer['email'], answer['content'], answer['is_right'])
    
    def to_entity(self) -> Answer:
        return Answer(self.exercise_id, self.email, self.content, self.is_right)
    
    def __repr__(self):
        return f"AnswerMongoDTO(exercise_id={self.exercise_id}, email={self.email}, content={self.content}, is_right={self.is_right})"
    
    def __eq__(self, other):
        if not isinstance(other, AnswerMongoDTO):
            return False
        return self.exercise_id == other.exercise_id and self.email == other.email and self.content == other.content and self.is_right == other.is_right