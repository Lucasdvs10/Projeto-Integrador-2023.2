from typing import List, Optional
from src.shared.domain.entities.exercise import Exercise
from src.shared.domain.repositories.exercise_repository_interface import IExerciseRepository


class ExerciseRepositoryMock(IExerciseRepository):
    def __init__(self) -> None:
        self._exercises = [
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

    def create_exercise(self, exercise: Exercise) -> Exercise:
        self._exercises.append(exercise)
        return exercise

    def get_exercise_by_id(self, exercise_id: str) -> Optional[Exercise]:
        for exercise in self._exercises:
            if exercise.exercise_id == exercise_id:
                return exercise
        return None

    def update_exercise_by_id(self, exercise_id: str, new_title: Optional[str] = None, new_enunciado: Optional[str] = None, new_creation_date: Optional[int] = None, new_expiration_date: Optional[int] = None, new_correct_answer: Optional[str] = None) -> Optional[Exercise]:
        exercise = self.get_exercise_by_id(exercise_id)

        if exercise is None:
            return None
        
        if new_title:
            exercise.title = new_title
        if new_enunciado:
            exercise.enunciado = new_enunciado
        if new_creation_date:
            exercise.creation_date = new_creation_date
        if new_expiration_date:
            exercise.expiration_date = new_expiration_date
        if new_correct_answer:
            exercise.correct_answer = new_correct_answer
            
        return exercise

    def delete_exercise_by_id(self, exercise_id: str) -> Optional[Exercise]:
        exercise_to_delete = self.get_exercise_by_id(exercise_id)
        
        if exercise_to_delete is None:
            return None

        self._exercises.remove(exercise_to_delete)
        return exercise_to_delete

    def get_all_exercises(self) -> List[Exercise]:
        return self._exercises