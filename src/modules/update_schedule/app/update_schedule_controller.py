from src.modules.update_schedule.app.update_schedule_usecase import UpdateScheduleUsecase
from src.modules.update_schedule.app.update_schedule_viewmodel import UpdateScheduleViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
import re


class UpdateScheduleController:
  def __init__(self, usecase: UpdateScheduleUsecase):
    self.usecase = usecase
    
  def __call__(self, request: HttpRequest) -> HttpResponse: 
    if not request.data.get("new_url"):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Field new_url is missing")
    if not re.search(r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&=\/]*)", request.data.get("new_url")):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Field new_url is invalid")
    
    new_schedule = self.usecase(new_url=request.data.get("new_url"))
    viewmodel = UpdateScheduleViewmodel(new_schedule)
    return OK(viewmodel.to_dict())
    
    # except MissingParameters as err:
    #   return BadRequest(body=err.message)
    
    # except EntityError as err:
    #   return BadRequest(body=err.message)
    
    # except Exception as err:
    #   return InternalServerError(body=err.args[0])