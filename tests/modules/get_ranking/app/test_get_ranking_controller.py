from src.modules.get_ranking.app.get_ranking_controller import GetRankingController
from src.modules.get_ranking.app.get_ranking_usecase import GetRankingUsecase
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetRankingController:
    
    def test_get_ranking_controller(self):
        repo = UserRepositoryMock()
        usecase = GetRankingUsecase(repo)
        controller = GetRankingController(usecase)
        response = controller(request={})
        expected = {'ranking': [{'rank': 1, 'email': '22.01049-0@maua.br', 'name': 'Vitor Negresiolo', 'role': 'STUDENT', 'exercises_solved': [1, 2, 3], 'points': 3}, {'rank': 2, 'email': '22.00680-0@maua.br', 'name': 'Rodrigo Siqueira', 'role': 'STUDENT', 'exercises_solved': [1, 2], 'points': 2}, {'rank': 3, 'email': '10.22533-7@maua.br', 'name': 'Doris Williams', 'role': 'STUDENT', 'exercises_solved': [], 'points': 0}, {'rank': 4, 'email': '21.37594-4@maua.br', 'name': 'David Davis', 'role': 'STUDENT', 'exercises_solved': [], 'points': 0}, {'rank': 5, 'email': '11.35709-7@maua.br', 'name': 'Michele Green', 'role': 'STUDENT', 'exercises_solved': [], 'points': 0}, {'rank': 6, 'email': '15.26374-2@maua.br', 'name': 'Anna Ethington', 'role': 'STUDENT', 'exercises_solved': [], 'points': 0}], 'message': 'Ranking retrieved successfully'}
        
        assert response.status_code == 200
        assert response.body == expected