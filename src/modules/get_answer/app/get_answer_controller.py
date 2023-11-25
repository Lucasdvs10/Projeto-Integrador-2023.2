from fastapi import HTTPException, status
from .get_answer_usecase import GetAnswerUsecase
from .get_answer_viewmodel import GetAnswerViewmodel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK


class GetAnswerController:
    def __init__(self, usecase: GetAnswerUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        answer_id = request.data.get("answer_id")
        if answer_id is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing answer id")
        if type(answer_id) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Answer id must be a string")
        
        answer = self.usecase(answer_id)
        viewmodel = GetAnswerViewmodel(answer)
        return OK(viewmodel.to_dict())