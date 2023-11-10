from src.shared.domain.entities.schedule import Schedule


class GetScheduleViewModel:
  schedule: Schedule
  
  def __init__(self, schedule: Schedule):
    self.schedule = schedule
  
  def to_dict(self) -> dict:
    return {
      "url": self.schedule.url
    }