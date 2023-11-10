from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.repositories.answer_repository_interface import IAnswerRepository
from src.shared.helpers.errors.domain_errors import EntityError
import re

class UpdateScheduleUsecase:
  def __init__(self, repo: IAnswerRepository):
    self.repo = repo
    
  def __call__(self, new_url: str) -> Schedule:
    if type(new_url) != str:
      raise EntityError("new_url")
    if not re.search(r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&=\/]*)", new_url):
      raise EntityError("new_url")
        
    return self.repo.update_schedule(new_url)
    
    