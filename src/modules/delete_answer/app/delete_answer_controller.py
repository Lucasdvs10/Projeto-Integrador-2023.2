from fastapi import HTTPException, status
from .delete_answer_usecase import DeleteAnswerUsecase
from .delete_answer_viewmodel import DeleteAnswerViewmodel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK


class DeleteAnswerController:
    def __init__(self, usecase: DeleteAnswerUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        answer_id = request.data.get("answer_id")
        if answer_id is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing answer id")
        if type(answer_id) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Answer id must be a string")
        
        answer = self.usecase(answer_id)
        viewmodel = DeleteAnswerViewmodel(answer)
        return OK(viewmodel.to_dict())