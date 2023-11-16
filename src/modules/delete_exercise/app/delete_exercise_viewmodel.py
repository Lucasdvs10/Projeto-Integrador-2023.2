from src.shared.domain.entities.exercise import Exercise


class ExerciseViewmodel:
    exercise_id: str
    title: str
    enunciado: str
    creation_date: int
    expiration_date: int
    correct_answer: str
    
    def __init__(self, exercise: Exercise):
        self.exercise_id = exercise.exercise_id
        self.title = exercise.title
        self.enunciado = exercise.enunciado
        self.creation_date = exercise.creation_date
        self.expiration_date = exercise.expiration_date
        self.correct_answer = exercise.correct_answer
        
    def to_dict(self):
        return {
            "exercise_id": self.exercise_id,
            "title": self.title,
            "enunciado": self.enunciado,
            "creation_date": self.creation_date,
            "expiration_date": self.expiration_date,
            "correct_answer": self.correct_answer
        }
        
class DeleteExerciseViewmodel:
    exercise: ExerciseViewmodel
    def __init__(self, exercise: Exercise):
        self.exercise = ExerciseViewmodel(exercise)
        
    def to_dict(self):
        return {
            "exercise": self.exercise.to_dict(),
            "message": "Exercise deleted successfully"
        }