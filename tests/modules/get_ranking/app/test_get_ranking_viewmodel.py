from src.modules.get_ranking.app.get_ranking_usecase import GetRankingUsecase
from src.modules.get_ranking.app.get_ranking_viewmodel import GetRankingViewmodel
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetRankingViewmodel:
    def test_get_ranking_viewmodel(self):
        repo = UserRepositoryMock()
        usecase = GetRankingUsecase(repo)

        ranking = usecase()
        viewmodel = GetRankingViewmodel(ranking).to_dict()
        
        assert viewmodel['message'] == 'Ranking retrieved successfully'
        assert len(viewmodel['ranking']) == len(ranking)
        assert all([viewmodel['ranking'][i]['points'] >= viewmodel['ranking'][i+1]['points'] for i in range(len(viewmodel['ranking'])-1)])
        assert all([viewmodel['ranking'][i]['rank'] == i+1 for i in range(len(viewmodel['ranking']))])
        assert all([viewmodel['ranking'][i]['points'] == len(viewmodel['ranking'][i]['exercises_solved']) for i in range(len(viewmodel['ranking']))])
        assert all([viewmodel['ranking'][i]['role'] == 'STUDENT' for i in range(len(viewmodel['ranking']))])