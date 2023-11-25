from .create_answer_usecase import CreateAnswerUsecase
from .create_answer_viewmodel import CreateAnswerViewmodel
from src.shared.domain.entities.answer import Answer
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from fastapi import HTTPException, status

from src.shared.helpers.external_interfaces.http_codes import Created

class CreateAnswerController:
    def __init__(self, usecase: CreateAnswerUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        if request.data.get('answer_id') is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Answer id is required")
        if type(request.data.get('answer_id')) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Answer id must be a string")
        
        if request.data.get('exercise_id') is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Exercise id is required")
        if type(request.data.get('exercise_id')) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Exercise id must be a string")
        
        if request.data.get('email') is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email is required")
        if type(request.data.get('email')) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email must be a string")

        if request.data.get('content') is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Enunciado is required")
        if type(request.data.get('content')) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Enunciado must be a string")
        if not Answer.MIN_CONTENT_LENGTH <= len(request.data.get('content')) <= Answer.MAX_CONTENT_LENGTH:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Enunciado must have between {Answer.MIN_CONTENT_LENGTH} and {Answer.MAX_CONTENT_LENGTH} characters")
        
        if request.data.get('is_right') is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Creation date is required")
        if type(request.data.get('is_right')) != int:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Creation date must be a decimal string")        
        
        answer = self.usecase(
            answer_id=request.data.get('answer_id'),
            exercise_id=request.data.get('exercise_id'),
            email=request.data.get('email'),
            content=request.data.get('content'),
            is_right=request.data.get('is_right'),
        )
        
        viewmodel = CreateAnswerViewmodel(answer)
        return Created(viewmodel.to_dict())