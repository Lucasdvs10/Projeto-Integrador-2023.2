from abc import abstractmethod
from typing import List, Optional

from src.shared.domain.entities.exercise import Exercise


class IExerciseRepository:
    @abstractmethod
    def create_exercise(self, exercise: Exercise) -> Exercise:
        pass

    @abstractmethod
    def get_exercise_by_id(self, exercise_id: str) -> Optional[Exercise]:
        pass

    @abstractmethod
    def update_exercise_by_id(self, exercise_id: str, new_title: Optional[str] = None, new_enunciado: Optional[str] = None, new_creation_date: Optional[int] = None, new_expiration_date: Optional[int] = None, new_correct_answer: Optional[str] = None) -> Optional[Exercise]:
        pass

    @abstractmethod
    def delete_exercise_by_id(self, id: str) -> Optional[Exercise]:
        pass
    
    @abstractmethod
    def get_all_exercises(self) -> List[Exercise]:
        pass