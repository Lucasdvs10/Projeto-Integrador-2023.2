from src.modules.get_ranking.app.get_ranking_presenter import get_ranking_presenter


class Test_GetRankingPresenter:
    def test_get_ranking_presenter(self):
        event = {}

        response = get_ranking_presenter(event, None)

        expected = {'ranking': [{'rank': 1, 'email': '22.01049-0@maua.br', 'name': 'Vitor Negresiolo', 'role': 'STUDENT', 'exercises_solved': [1, 2, 3], 'points': 3}, {'rank': 2, 'email': '22.00680-0@maua.br', 'name': 'Rodrigo Siqueira', 'role': 'STUDENT', 'exercises_solved': [1, 2], 'points': 2}], 'message': 'Ranking retrieved successfully'}
    
        assert response["body"] == expected
        assert response["status_code"] == 200