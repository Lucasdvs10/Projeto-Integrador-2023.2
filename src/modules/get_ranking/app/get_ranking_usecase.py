from src.shared.domain.repositories.user_repository_interface import IUserRepository


class GetRankingUsecase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo
        
    def __call__(self) -> list:
        users = self.repo.get_all_users()
        users.sort(key=lambda x: x.exercises_solved, reverse=True)
        ranking = []
        for i in range(len(users)):
            ranking.append((i+1, users[i]))
        return ranking