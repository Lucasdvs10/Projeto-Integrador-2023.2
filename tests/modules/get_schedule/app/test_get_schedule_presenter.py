import json
from src.modules.get_schedule.app.get_schedule_presenter import get_shedule_presenter


class Test_GetSchedulePresenter:
  def test_get_schedule_presenter(self):
    event = {}
    
    response = get_shedule_presenter(event, None)
    
    expected = {
      "url": "https://www.google.com"
    }
    
    assert response["body"] == expected
    