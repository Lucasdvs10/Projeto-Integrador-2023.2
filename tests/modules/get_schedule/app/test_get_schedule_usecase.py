from src.modules.get_schedule.app.get_schedule_usecase import GetScheduleUsecase
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


class Test_GetScheduleUsecase:
  def test_get_schedule_usecase(self):
    repo = AnswerRepositoryMock()
    usecase = GetScheduleUsecase(repo)
    
    schedule = usecase()
    
    assert schedule.url == 'https://www.google.com'
    