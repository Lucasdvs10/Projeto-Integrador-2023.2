from fastapi import HTTPException, status
from src.shared.domain.entities.answer import Answer
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK
from .update_answer_viewmodel import UpdateAnswerViewmodel
from .update_answer_usecase import UpdateAnswerUsecase


class UpdateAnswerController:
    def __init__(self, usecase: UpdateAnswerUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        if 'answer_id' in request.data.keys():
            if request.data.get("answer_id") is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Answer id can't be None")
            
            if type(request.data.get("answer_id")) != str:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Answer id must be a string")
            
        if 'new_content' in request.data.keys():
            if request.data.get("new_content") is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New content can't be None")
            
            if type(request.data.get("new_content")) != str:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New content must be a string")
            
            if not Answer.MIN_CONTENT_LENGTH <= len(request.data.get("new_content")) <= Answer.MAX_CONTENT_LENGTH:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"New content must be between {Answer.MIN_CONTENT_LENGTH} and {Answer.MAX_CONTENT_LENGTH} characters")
            
        if 'new_email' in request.data.keys():
            if request.data.get("new_email") is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New email can't be None")
            
            if type(request.data.get("new_email")) != str:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New email must be a string")
            
        if 'new_is_right' in request.data.keys():
            if request.data.get("new_is_right") is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New is right can't be None")
            
            if type(request.data.get("new_is_right")) != int:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New is right must be an integer")
              
        updated_answer = self.usecase(
            answer_id=request.data.get("answer_id"),
            new_content=request.data.get("new_content"),
            new_email=request.data.get("new_email"),
            new_is_right=request.data.get("new_is_right")
        )
        
        viewmodel = UpdateAnswerViewmodel(updated_answer)
        
        return OK(viewmodel.to_dict())