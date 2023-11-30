from src.shared.helpers.external_interfaces.http_codes import OK
from .validate_answer_viewmodel import ValidateAnswerViewmodel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from .validate_answer_usecase import ValidateAnswerUsecase
from fastapi import HTTPException, status

class ValidateAnswerController:
    def __init__(self, usecase: ValidateAnswerUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        if request.data.get("answer_id") is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing answer_id")
        if type(request.data.get("answer_id")) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid answer_id")
        
        if request.data.get("is_right") is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing is_right")
        if request.data.get("is_right") not in [0, 1]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid is_right")
        
        answer = self.usecase(request.data.get("answer_id"), request.data.get("is_right"))
        viewmodel = ValidateAnswerViewmodel(answer)
        return OK(viewmodel)