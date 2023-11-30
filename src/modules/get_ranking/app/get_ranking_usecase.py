from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.user_repository_interface import IUserRepository


class GetRankingUsecase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo
        
    def __call__(self) -> list:
        users = self.repo.get_all_users()
        users.sort(key=lambda x: len(x.exercises_solved), reverse=True)
        ranking = []
        rank = 1
        for i in range(len(users)):
            if users[i] != None and users[i].role == ROLE.STUDENT:
                ranking.append((rank, users[i]))
                rank += 1
                
        return ranking