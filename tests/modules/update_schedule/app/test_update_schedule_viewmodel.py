from src.modules.update_schedule.app.update_schedule_usecase import UpdateScheduleUsecase
from src.modules.update_schedule.app.update_schedule_viewmodel import UpdateScheduleViewmodel
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


class Test_UpdateScheduleViewmodel:
  def test_update_schedule_viewmodel(self):
    repo = AnswerRepositoryMock()
    usecase = UpdateScheduleUsecase(repo)    
    new_schedule = usecase("https://www.youtube.com")
    
    viewmodel = UpdateScheduleViewmodel(new_schedule)
    
    expected = {
      "url": "https://www.youtube.com",
      "message": "Schedule updated successfully!"
    }
    
    assert viewmodel.to_dict() == expected
  