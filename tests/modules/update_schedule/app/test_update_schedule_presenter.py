from src.modules.update_schedule.app.update_schedule_presenter import update_schedule_presenter
from fastapi import HTTPException
import pytest

class Test_UpdateSchedulePresenter:
  def test_update_schedule_presenter(self):
    event = {
      'body': {
        'new_url': 'https://www.youtube.com'
      }
    }
    
    response = update_schedule_presenter(event, None)
    
    expected = {
      'url': 'https://www.youtube.com',
      'message': 'Schedule updated successfully!'
    }
    
    assert response["body"] == expected
    
  def test_update_schedule_presenter_without_url(self):
    event = {
      'body': {}
    }
    
    with pytest.raises(HTTPException):
      update_schedule_presenter(event, None)
    
    