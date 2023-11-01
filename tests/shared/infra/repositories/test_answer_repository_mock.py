from src.shared.domain.repositories.answer_repository_mock import AnswerRepositoryMock


class Test_AnswerRepositoryMock:
  def test_get_answers(self):
    repo = AnswerRepositoryMock()
    
    answers = repo.get_answers()
    
    assert repo.get_answers() == repo.all_answers
    assert len(answers) == 6