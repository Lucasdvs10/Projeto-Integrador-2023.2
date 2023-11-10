from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.repositories.answer_repository_interface import IAnswerRepository


class GetScheduleUsecase:
  def __init__(self, repo: IAnswerRepository):
    self.repo = repo
    
  def __call__(self) -> Schedule:
    return self.repo.get_schedule()