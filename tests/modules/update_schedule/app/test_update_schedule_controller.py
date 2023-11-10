from src.modules.update_schedule.app.update_schedule_controller import UpdateScheduleController
from src.modules.update_schedule.app.update_schedule_usecase import UpdateScheduleUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock
from fastapi import HTTPException
import pytest


class Test_UpdateScheduleController:
  def test_update_schedule_controller(self):
    repo = AnswerRepositoryMock()
    usecase = UpdateScheduleUsecase(repo)
    controller = UpdateScheduleController(usecase)
    
    request = HttpRequest(
      body={
        "new_url": "https://www.youtube.com"
      }
    )
    
    response = controller(request=request)
    
    assert response.status_code == 200
    assert response.body == {
      "url": "https://www.youtube.com",
      "message": "Schedule updated successfully!"
    }
    
  def test_update_schedule_controller_invalid(self):
    repo = AnswerRepositoryMock()
    usecase = UpdateScheduleUsecase(repo)
    controller = UpdateScheduleController(usecase)
    
    request = HttpRequest(
      body={}
    )
    
    with pytest.raises(HTTPException):
      controller(request=request)
  