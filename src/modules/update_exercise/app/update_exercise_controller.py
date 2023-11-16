from fastapi import HTTPException, status
from src.shared.domain.entities.exercise import Exercise
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK
from .update_exercise_viewmodel import UpdateExerciseViewmodel
from .update_exercise_usecase import UpdateExerciseUsecase


class UpdateExerciseController:
    def __init__(self, usecase: UpdateExerciseUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        if request.data.get("exercise_id") is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing exercise_id")
        
        if type(request.data.get("exercise_id")) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid exercise_id")
        
        if 'new_title' in request.data.keys():
            if request.data.get("new_title") is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title can't be None")
            
            if type(request.data.get("new_title")) != str:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New title must be a string")
            
            if not Exercise.MIN_TITLE_LENGTH <= len(request.data.get("new_title")) <= Exercise.MAX_TITLE_LENGTH:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"New title must be between {Exercise.MIN_TITLE_LENGTH} and {Exercise.MAX_TITLE_LENGTH} characters")
            
        if 'new_enunciado' in request.data.keys():
            if request.data.get("new_enunciado") is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Enunciado can't be None")
            
            if type(request.data.get("new_enunciado")) != str:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New enunciado must be a string")
            
            if not Exercise.MIN_ENUNCIADO_LENGTH <= len(request.data.get("new_enunciado")) <= Exercise.MAX_ENUNCIADO_LENGTH:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"New enunciado must be between {Exercise.MIN_ENUNCIADO_LENGTH} and {Exercise.MAX_ENUNCIADO_LENGTH} characters")
            
        if 'new_creation_date' in request.data.keys():
            if request.data.get("new_creation_date") is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Creation date can't be None")
            
            if type(request.data.get("new_creation_date")) != int:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New creation date must be an integer")
            
            if not 1577847600000 <= request.data.get("new_creation_date") <= 3387133800000:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New creation date must be between 2020-01-01 and 2077-05-01")
            
        if 'new_expiration_date' in request.data.keys():
            if request.data.get("new_expiration_date") is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Expiration date can't be None")
            
            if type(request.data.get("new_expiration_date")) != int:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New expiration date must be an integer")
            
            if not 1577847600000 <= request.data.get("new_expiration_date") <= 3387133800000:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New expiration date must be between 2020-01-01 and 2077-05-01")
            
        if 'new_correct_answer' in request.data.keys():
            if request.data.get("new_correct_answer") is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Correct answer can't be None")
            
            if type(request.data.get("new_correct_answer")) != str:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New correct answer must be a string")

            if len(request.data.get("new_correct_answer")) < 1:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New correct answer can't be empty")
            
        updated_exercise = self.usecase(
            exercise_id=request.data.get("exercise_id"),
            new_title=request.data.get("new_title"),
            new_enunciado=request.data.get("new_enunciado"),
            new_creation_date=request.data.get("new_creation_date"),
            new_expiration_date=request.data.get("new_expiration_date"),
            new_correct_answer=request.data.get("new_correct_answer")
        )
        
        viewmodel = UpdateExerciseViewmodel(updated_exercise)
        
        return OK(viewmodel.to_dict())