from .get_ranking_controller import GetRankingController
from .get_ranking_usecase import GetRankingUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


def get_ranking_presenter(event, context):
  repo = UserRepositoryMock()
  usecase = GetRankingUsecase(repo)
  controller = GetRankingController(usecase)
  
  httpRequest = FastAPIHttpRequest(data=event)
  response = controller(httpRequest)
  httpResponse = FastAPIHttpResponse(
    body=response.body, status_code=response.status_code, headers=response.headers
  )
  
  return httpResponse.to_dict()