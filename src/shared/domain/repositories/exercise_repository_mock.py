from datetime import  datetime
from typing import Optional
from src.shared.domain.entities.exercise import Exercise
from src.shared.domain.repositories.exercise_repository_interface import IExerciseRepository


class ExerciseRepositoryMock(IExerciseRepository):
    def __init__(self) -> None:
        self.all_exercises = [
                Exercise(exercise_id="111-111-111",
                         discipline_id="777-888-999",
                         title="Primeiro Presidente do Brasil",
                         enunciado="Quem foi o primeiro presidente do Brasil?",
                         creation_date=datetime(2023, 1,10),
                         exipiration_date=datetime(2023, 2, 10),
                         correct_answer="Marechal Deodoro"
                         ),
                Exercise(exercise_id="111-222-111",
                         discipline_id="777-888-l01010",
                         title="Qual lingua é mais antiga",
                         enunciado="Qual lingua é mais antiga: Python ou java",
                         creation_date=datetime(2023, 1,10),
                         exipiration_date=datetime(2023, 2, 11),
                         correct_answer="Python"
                         )
        ]

    def create_exercise(self, exercise: Exercise) -> Exercise:
        self.all_exercises.append(exercise)
        return exercise

    def get_exercise_by_id(self, id: str) -> Optional[Exercise]:
        for exercise in self.all_exercises:
            if exercise.exercise_id == id:
                return exercise
        return None

    def update_exercise_by_id(self) -> Optional[Exercise]:
        pass

    def delete_exercise_by_id(self, id: str) -> Optional[Exercise]:
        exercise_to_delete = self.get_exercise_by_id(id)
        
        if exercise_to_delete is None:
            return None

        self.all_exercises.remove(exercise_to_delete)
        return exercise_to_delete
