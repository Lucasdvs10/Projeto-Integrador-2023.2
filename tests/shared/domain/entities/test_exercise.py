from datetime import datetime
from src.shared.domain.entities.exercise import Exercise


class Test_Exercise:
    current_time = int(datetime.now().timestamp() * 1000)
    def test_instantiate_exercise(self):
        exercise = Exercise(exercise_id="aisdjasdjiou", title="Exercicio 1", enunciado="Enunciado do exercicio 1", creation_date=self.current_time,expiration_date=self.current_time + 604800000, correct_answer="Resposta correta")
        assert exercise is not None
        
    def test_change_exercise_id(self):
        exercise = Exercise(exercise_id="aisdjasdjiou", title="Exercicio 1", enunciado="Enunciado do exercicio 1", creation_date=self.current_time,expiration_date=self.current_time + 604800000, correct_answer="Resposta correta")
        
        exercise.exercise_id = "aisdjasdjiou2"
        assert exercise.exercise_id == "aisdjasdjiou2"
        
    def test_change_title(self):
        exercise = Exercise(exercise_id="aisdjasdjiou", title="Exercicio 1", enunciado="Enunciado do exercicio 1", creation_date=self.current_time,expiration_date=self.current_time + 604800000, correct_answer="Resposta correta")
        
        exercise.title = "Exercicio 2"
        assert exercise.title == "Exercicio 2"
        
    def test_change_enunciado(self):
        exercise = Exercise(exercise_id="aisdjasdjiou", title="Exercicio 1", enunciado="Enunciado do exercicio 1", creation_date=self.current_time,expiration_date=self.current_time + 604800000, correct_answer="Resposta correta")
        
        exercise.enunciado = "Enunciado do exercicio 2"
        assert exercise.enunciado == "Enunciado do exercicio 2"
        
    def test_change_creation_date(self):
        exercise = Exercise(exercise_id="aisdjasdjiou", title="Exercicio 1", enunciado="Enunciado do exercicio 1", creation_date=self.current_time,expiration_date=self.current_time + 604800000, correct_answer="Resposta correta")
        
        exercise.creation_date = self.current_time + 1000
        assert exercise.creation_date == self.current_time + 1000
        
    def test_change_expiration_date(self):
        exercise = Exercise(exercise_id="aisdjasdjiou", title="Exercicio 1", enunciado="Enunciado do exercicio 1", creation_date=self.current_time,expiration_date=self.current_time + 604800000, correct_answer="Resposta correta")
        
        exercise.expiration_date = self.current_time + 604800000 + 1000
        assert exercise.expiration_date == self.current_time + 604800000 + 1000
        
    def test_change_correct_answer(self):
        exercise = Exercise(exercise_id="aisdjasdjiou", title="Exercicio 1", enunciado="Enunciado do exercicio 1", creation_date=self.current_time,expiration_date=self.current_time + 604800000, correct_answer="Resposta correta")
        
        exercise.correct_answer = "Resposta correta 2"
        assert exercise.correct_answer == "Resposta correta 2"