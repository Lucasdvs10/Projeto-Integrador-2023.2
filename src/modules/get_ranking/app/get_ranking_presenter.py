from .get_ranking_controller import GetRankingController
from .get_ranking_usecase import GetRankingUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.environments import Environments

def get_ranking_presenter(event, context):
  repo = Environments.get_user_repo()()
  usecase = GetRankingUsecase(repo)
  controller = GetRankingController(usecase)
  
  httpRequest = FastAPIHttpRequest(data=event)
  response = controller(httpRequest)
  httpResponse = FastAPIHttpResponse(
    body=response.body, status_code=response.status_code, headers=response.headers
  )
  
  return httpResponse.to_dict()