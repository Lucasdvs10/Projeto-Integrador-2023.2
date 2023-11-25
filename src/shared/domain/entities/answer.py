import dataclasses

from src.shared.helpers.errors.domain_errors import EntityParameterTypeError

@dataclasses.dataclass
class Answer:
  _answer_id: str
  _exercise_id: str
  _email: str
  _content: str
  _is_right: 0 | 1
  MIN_CONTENT_LENGTH = 3
  MAX_CONTENT_LENGTH = 300
  
  def __init__(self, answer_id, exercise_id, email, content, is_right):
    if (type(answer_id) != str):
      raise EntityParameterTypeError("Answer_id")
    self._answer_id = answer_id
    if (type(exercise_id) != str):
      raise EntityParameterTypeError("Exercise_id")
    self._exercise_id = exercise_id
    if (type(email) != str):
      raise EntityParameterTypeError("Email")
    self._email = email
    if (type(content) != str):
      raise EntityParameterTypeError("Content")
    self._content = content
    if (type(is_right) != int and is_right != 0 and is_right != 1):
      raise EntityParameterTypeError("Is_right")
    self._is_right = is_right
  
  @property
  def answer_id(self):
    return self._answer_id
  
  @answer_id.setter
  def answer_id(self, value):
    if (type(value) != str):
      raise EntityParameterTypeError("Answer_id")
    self._answer_id = value
    
  @property
  def exercise_id(self):
    return self._exercise_id
  
  @exercise_id.setter
  def exercise_id(self, value):
    if (type(value) != str):
      raise EntityParameterTypeError("Exercise_id")
    self._exercise_id = value
  
  @property
  def email(self):
    return self._email
  
  @email.setter
  def email(self, value):
    if (type(value) != str):
      raise EntityParameterTypeError("Email")
    self._email = value
  
  @property
  def content(self):
    return self._content
  
  @content.setter
  def content(self, value):
    if (type(value) != str):
      raise EntityParameterTypeError("Content")
    self._content = value
  
  @property
  def is_right(self):
    return self._is_right
  
  @is_right.setter
  def is_right(self, value):
    if (type(value) != int and value != 0 and value != 1):
      raise EntityParameterTypeError("Is_right")
    self._is_right = value