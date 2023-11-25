import pytest

from src.shared.domain.entities.answer import Answer
from src.shared.helpers.errors.domain_errors import EntityParameterTypeError

class Test_Answer:
  def test_instantiate_answer(self):
    answer = Answer(answer_id="aisdjasdjiou", exercise_id="111-555-111", email="email", content="content", is_right=1)
    
    assert answer is not None
    
  def test_change_answer_id(self):
    answer = Answer(answer_id="aisdjasdjiou", exercise_id="111-555-111", email="email", content="content", is_right=1)
    
    answer.answer_id = "new_id"
    
    assert answer.answer_id == "new_id"
    
  def test_change_answer_id_to_a_invalid_one(self):
    answer = Answer(answer_id="aisdjasdjiou", exercise_id="111-555-111", email="email", content="content", is_right=1)
    
    with(pytest.raises(EntityParameterTypeError)):
      answer.answer_id = 1996
  
  def test_change_answer_email(self):
    answer = Answer(answer_id="aisdjasdjiou", exercise_id="111-555-111",email="email", content="content", is_right=1)
    
    answer.email = "new_email"
    
    assert answer.email == "new_email"
  
  def test_change_answer_email_to_a_invalid_one(self):
    answer = Answer(answer_id="aisdjasdjiou", exercise_id="111-555-111", email="email", content="content", is_right=1)
    
    with(pytest.raises(EntityParameterTypeError)):
      answer.email = 1996
  
  def test_change_answer_content(self):
    answer = Answer(answer_id="aisdjasdjiou", exercise_id="111-555-111", email="email", content="content", is_right=1)
    
    answer.content = "new_content"
    
    assert answer.content == "new_content"
    
  def test_change_answer_content_to_a_invalid_one(self):
    answer = Answer(answer_id="aisdjasdjiou", exercise_id="111-555-111", email="email", content="content", is_right=1)
    
    with(pytest.raises(EntityParameterTypeError)):
      answer.content = 1996
  
  def test_change_answer_is_right(self):
    answer = Answer(answer_id="aisdjasdjiou", exercise_id="111-555-111", email="email", content="content", is_right=1)
    
    answer.is_right = 0
    
    assert answer.is_right == 0
    
  def test_change_answer_is_right_to_a_invalid_one(self):
    answer = Answer(answer_id="aisdjasdjiou", exercise_id="111-555-111", email="email", content="content", is_right=1)
    
    with(pytest.raises(EntityParameterTypeError)):
      answer.is_right = "Uma string"
      