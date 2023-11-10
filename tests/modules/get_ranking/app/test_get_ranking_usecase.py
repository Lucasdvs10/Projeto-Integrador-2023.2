from src.modules.get_ranking.app.get_ranking_usecase import GetRankingUsecase
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetRankingUsecase:
    def test_get_ranking_usecase(self):
        repo = UserRepositoryMock()
        usecase = GetRankingUsecase(repo)
        
        ranking = usecase()
        
        assert len(ranking) == len(repo._users)
        assert all([ranking[i][1].exercises_solved >= ranking[i+1][1].exercises_solved for i in range(len(ranking)-1)])
        assert all([ranking[i][0] == i+1 for i in range(len(ranking))])