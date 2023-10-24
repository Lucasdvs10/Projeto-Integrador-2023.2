from abc import abstractmethod
from typing import Optional

from src.shared.domain.entities.exercise import Exercise


class IExerciseRepository:
    @abstractmethod
    def create_exercise(self, exercise: Exercise) -> Exercise:
        pass

    @abstractmethod
    def get_exercise_by_id(self, id: str) -> Optional[Exercise]:
        pass

    @abstractmethod
    def update_exercise_by_id(self) -> Optional[Exercise]:
        pass

    @abstractmethod
    def delete_exercise_by_id(self, id: str) -> Optional[Exercise]:
        pass
