from src.modules.get_ranking.app.get_ranking_controller import GetRankingController
from src.modules.get_ranking.app.get_ranking_usecase import GetRankingUsecase
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetRankingController:
    
    def test_get_ranking_controller(self):
        repo = UserRepositoryMock()
        usecase = GetRankingUsecase(repo)
        controller = GetRankingController(usecase)
        response = controller(request={})
        
        assert response.status_code == 200
        assert len(response.body["ranking"]) == len([user for user in response.body["ranking"] if user["role"] == 'STUDENT'])
        assert all([response.body["ranking"][i]["exercises_solved"] >= response.body["ranking"][i+1]["exercises_solved"] for i in range(len(response.body["ranking"])-1)])