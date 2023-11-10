from src.modules.update_schedule.app.update_schedule_controller import UpdateScheduleController
from src.modules.update_schedule.app.update_schedule_usecase import UpdateScheduleUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


def update_schedule_presenter(event, context):
  repo = AnswerRepositoryMock()
  usecase = UpdateScheduleUsecase(repo)
  controller = UpdateScheduleController(usecase)
  
  httpRequest = FastAPIHttpRequest(data=event)
  response = controller(httpRequest)
  httpResponse = FastAPIHttpResponse(
    body=response.body, status_code=response.status_code, headers=response.headers
  )
  
  return httpResponse.to_dict()