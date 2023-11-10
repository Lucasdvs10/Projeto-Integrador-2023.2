from src.modules.get_schedule.app.get_schedule_usecase import GetScheduleUsecase
from src.modules.get_schedule.app.get_schedule_viewmodel import GetScheduleViewModel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, InternalServerError


class GetScheduleController:
  
  def __init__(self, usecase: GetScheduleUsecase):
    self.usecase = usecase
    
  def __call__(self, request: IRequest) -> IResponse:
    try:
      schedule = self.usecase()
      viewmodel = GetScheduleViewModel(schedule)
      return OK(viewmodel.to_dict())
    
    except Exception as err:
      return InternalServerError(body=err.args[0])