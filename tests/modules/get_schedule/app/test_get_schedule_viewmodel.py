from src.modules.get_schedule.app.get_schedule_usecase import GetScheduleUsecase
from src.modules.get_schedule.app.get_schedule_viewmodel import GetScheduleViewModel
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


class Test_GetScheduleViewmodel:
  def test_get_schedule_viewmodel(self):
    repo = AnswerRepositoryMock()
    usecase = GetScheduleUsecase(repo)
    schedule = usecase()
    viewmodel = GetScheduleViewModel(schedule)
    
    expected = {
      "url": "https://www.google.com"
    }
    
    assert viewmodel.to_dict() == expected