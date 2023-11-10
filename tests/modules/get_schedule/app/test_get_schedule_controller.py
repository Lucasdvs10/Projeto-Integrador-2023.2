from src.modules.get_schedule.app.get_schedule_controller import GetScheduleController
from src.modules.get_schedule.app.get_schedule_usecase import GetScheduleUsecase
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


class Test_GetScheduleCOntroller:
  def test_get_schedule_controller(self):
    repo = AnswerRepositoryMock()
    usecase = GetScheduleUsecase(repo)
    controller = GetScheduleController(usecase)
    
    response = controller(request={})
    
    assert response.status_code == 200
    assert response.body == {
      "url": "https://www.google.com"
    }
    
    