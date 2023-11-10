from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock
from src.modules.get_schedule.app.get_schedule_usecase import GetScheduleUsecase
from src.modules.get_schedule.app.get_schedule_controller import GetScheduleController
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse


def get_shedule_presenter(event, context):
  repo = AnswerRepositoryMock()
  usecase = GetScheduleUsecase(repo)
  controller = GetScheduleController(usecase)
  
  httpRequest = FastAPIHttpRequest(data=event)
  response = controller(httpRequest)
  httpResponse = FastAPIHttpResponse(
    body=response.body, status_code=response.status_code, headers=response.headers
  )
  
  return httpResponse.to_dict()