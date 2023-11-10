from typing import List, Tuple
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE


class UserViewmodel:
    rank: int
    email: str
    name: str
    role: ROLE
    exercises_solved : List[str]
    points: int
    
    def __init__(self, user_tuple: Tuple[int, User]):
        self.rank = user_tuple[0]
        self.email = user_tuple[1].email
        self.name = user_tuple[1].name
        self.role = user_tuple[1].role
        self.exercises_solved = user_tuple[1].exercises_solved
        self.points = len(user_tuple[1].exercises_solved)
        
    def to_dict(self):
        return {
            "rank": self.rank,
            "email": self.email,
            "name": self.name,
            "role": self.role.value,
            "exercises_solved": self.exercises_solved,
            "points": self.points
        }
        
class GetRankingViewmodel:
    ranking: List[UserViewmodel]
    
    def __init__(self, ranking: List[Tuple[int, User]]):
        self.ranking = [UserViewmodel(user) for user in ranking]
        
    def to_dict(self):
        return {
            "ranking": [user.to_dict() for user in self.ranking],
            "message": "Ranking retrieved successfully"
        }