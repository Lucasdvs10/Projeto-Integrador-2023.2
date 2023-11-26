from src.shared.domain.entities.exercise import Exercise


class ExerciseMongoDTO:
    exercise_id: str
    title: str
    enunciado: str
    creation_date: int # milliseconds
    expiration_date: int # milliseconds
    correct_answer: str
    
    def __init__(self, exercise_id, title, enunciado, creation_date, expiration_date, correct_answer):
        self.exercise_id = exercise_id
        self.title = title
        self.enunciado = enunciado
        self.creation_date = creation_date
        self.expiration_date = expiration_date
        self.correct_answer = correct_answer
        
    @staticmethod
    def from_entity(exercise: Exercise) -> 'ExerciseMongoDTO':
        return ExerciseMongoDTO(exercise.exercise_id, exercise.title, exercise.enunciado, exercise.creation_date, exercise.expiration_date, exercise.correct_answer)
    
    def to_mongo(self) -> dict:
        return {
            'exercise_id': self.exercise_id,
            'title': self.title,
            'enunciado': self.enunciado,
            'creation_date': self.creation_date,
            'expiration_date': self.expiration_date,
            'correct_answer': self.correct_answer
        }
        
    @staticmethod
    def from_mongo(exercise: dict) -> 'ExerciseMongoDTO':
        return ExerciseMongoDTO(exercise['exercise_id'], exercise['title'], exercise['enunciado'], int(exercise['creation_date']), int(exercise['expiration_date']), exercise['correct_answer'])
    
    def to_entity(self) -> Exercise:
        return Exercise(self.exercise_id, self.title, self.enunciado, self.creation_date, self.expiration_date, self.correct_answer)
    
    def __repr__(self):
        return f"ExerciseMongoDTO(exercise_id={self.exercise_id}, title={self.title}, enunciado={self.enunciado}, creation_date={self.creation_date}, expiration_date={self.expiration_date}, correct_answer={self.correct_answer})"
    
    def __eq__(self, other):
        if not isinstance(other, ExerciseMongoDTO):
            return False
        return self.exercise_id == other.exercise_id and self.title == other.title and self.enunciado == other.enunciado and self.creation_date == other.creation_date and self.expiration_date == other.expiration_date and self.correct_answer == other.correct_answer