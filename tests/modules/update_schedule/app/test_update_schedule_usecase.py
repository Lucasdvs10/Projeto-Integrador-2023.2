from src.modules.get_schedule.app.get_schedule_usecase import GetScheduleUsecase
from src.modules.update_schedule.app.update_schedule_usecase import UpdateScheduleUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock
import pytest


class Test_UpdateScheduleUsecase:
  def test_update_schedule_usecase(self):
    repo = AnswerRepositoryMock()
    usecase = UpdateScheduleUsecase(repo)
    get_schedule_usecase = GetScheduleUsecase(repo)
    
    old_schedule = get_schedule_usecase()
    new_schedule = usecase("https://www.youtube.com")
    
    assert old_schedule.url != new_schedule.url
    
  def test_update_schedule_usecase_invalid(self):
    repo = AnswerRepositoryMock()
    usecase = UpdateScheduleUsecase(repo)
    
    with pytest.raises(EntityError):
      usecase(123)
      
  def test_update_schedule_usecase_invalid_url(self):
    repo = AnswerRepositoryMock()
    usecase = UpdateScheduleUsecase(repo)
    
    with pytest.raises(EntityError):
      usecase("123")
    
    