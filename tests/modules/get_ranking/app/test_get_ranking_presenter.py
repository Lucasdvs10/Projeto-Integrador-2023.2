from src.modules.get_ranking.app.get_ranking_presenter import get_ranking_presenter


class Test_GetRankingPresenter:
    def test_get_ranking_presenter(self):
        event = {}

        response = get_ranking_presenter(event, None)

        assert response["status_code"] == 200
        assert len(response["body"]["ranking"]) == len([user for user in response["body"]["ranking"] if user["role"] == 'STUDENT'])
        assert all([response["body"]["ranking"][i]["exercises_solved"] >= response["body"]["ranking"][i+1]["exercises_solved"] for i in range(len(response["body"]["ranking"])-1)])