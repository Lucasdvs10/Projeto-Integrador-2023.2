from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.entities.answer import Answer
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock


class Test_AnswerRepositoryMock:
  def test_get_answers(self):
    repo = AnswerRepositoryMock()
    
    answers = repo.get_answers("111-111-111")

    assert len(answers) == 4
    
  def test_get_schedule(self):
    repo = AnswerRepositoryMock()
    
    schedule = repo.get_schedule()
    
    assert schedule == repo.schedule
    assert schedule.url == "https://www.google.com"
    assert type(schedule.url) == str
    
  def test_update_schedule(self):
    repo = AnswerRepositoryMock()
    
    schedule = repo.get_schedule()
    
    repo.update_schedule("https://www.youtube.com")
    
    new_schedule = repo.get_schedule()
    
    assert new_schedule != schedule
    assert new_schedule.url == "https://www.youtube.com"
    assert type(new_schedule.url) == str
    
  def test_create_answer(self):
    repo = AnswerRepositoryMock()
    
    old_len = len(repo.all_answers)
    
    answer = Answer("7", "111-555-111", "email", "content", 0)
    
    repo.create_answer(answer)
    
    assert len(repo.all_answers) == 9
    assert len(repo.all_answers) != old_len
    
  def test_get_answer(self):
    repo = AnswerRepositoryMock()
    
    answer = repo.get_answer("0")
        
    assert answer.answer_id == "0"
    assert answer.exercise_id == "111-111-111"
    assert answer.email == "umemail@gmail.com"
    assert answer.content == "A resposta vem aqui!"
    assert answer.is_right == 0
    
  def test_update_answer(self):
    repo = AnswerRepositoryMock()
    
    answer = repo.get_answer("1")
    
    new_answer = repo.update_answer("1", "new one", "new email", 1)
    
    assert new_answer.answer_id == "1"
    assert new_answer.email == "new email"
    assert new_answer.content == "new one"
    assert new_answer.is_right == 1
    
  def test_delete_answer_by_id(self):
    repo = AnswerRepositoryMock()
    
    old_len = len(repo.all_answers)
    
    repo.delete_answer("1")
    
    assert old_len == 8
    assert len(repo.all_answers) == 7
    
    
    