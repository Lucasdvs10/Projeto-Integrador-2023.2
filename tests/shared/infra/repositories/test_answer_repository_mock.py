from src.shared.domain.entities.schedule import Schedule
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


class Test_AnswerRepositoryMock:
  def test_get_answers(self):
    repo = AnswerRepositoryMock()
    
    answers = repo.get_answers()
    
    assert repo.get_answers() == repo.all_answers
    assert len(answers) == 6
    
  def test_get_schedule(self):
    repo = AnswerRepositoryMock()
    
    schedule = repo.get_schedule()
    
    assert schedule == repo.schedule
    assert schedule.url == "https://www.google.com"
    assert type(schedule.url) == str
    
  def test_update_schedule(self):
    repo = AnswerRepositoryMock()
    
    schedule = repo.get_schedule()
    
    repo.update_schedule(Schedule("https://www.youtube.com"))
    
    new_schedule = repo.get_schedule()
    
    assert new_schedule != schedule
    assert new_schedule.url == "https://www.youtube.com"
    assert type(new_schedule.url) == str
    
    