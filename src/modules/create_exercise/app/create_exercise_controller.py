from .create_exercise_usecase import CreateExerciseUseCase
from .create_exercise_viewmodel import CreateExerciseViewmodel
from src.shared.domain.entities.exercise import Exercise
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from fastapi import HTTPException, status

from src.shared.helpers.external_interfaces.http_codes import Created

class CreateExerciseController:
    def __init__(self, usecase: CreateExerciseUseCase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        if request.data.get('exercise_id') is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Exercise id is required")
        if type(request.data.get('exercise_id')) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Exercise id must be a string")
        
        if request.data.get('title') is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title is required")
        if type(request.data.get('title')) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title must be a string")
        if not Exercise.MIN_TITLE_LENGTH <= len(request.data.get('title')) <= Exercise.MAX_TITLE_LENGTH:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Title must have between {Exercise.MIN_TITLE_LENGTH} and {Exercise.MAX_TITLE_LENGTH} characters")

        if request.data.get('enunciado') is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Enunciado is required")
        if type(request.data.get('enunciado')) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Enunciado must be a string")
        if not Exercise.MIN_ENUNCIADO_LENGTH <= len(request.data.get('enunciado')) <= Exercise.MAX_ENUNCIADO_LENGTH:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Enunciado must have between {Exercise.MIN_ENUNCIADO_LENGTH} and {Exercise.MAX_ENUNCIADO_LENGTH} characters")
        
        if request.data.get('creation_date') is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Creation date is required")
        if type(request.data.get('creation_date')) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Creation date must be a decimal string")
        if request.data.get('creation_date').isdecimal() == False:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Creation date must be a decimal string")
        creation_date = int(request.data.get('creation_date'))
        if not 1577847600000 <= creation_date <= 3387133800000:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Creation date must be between 2020-01-01 and 2077-05-01")
        
        if request.data.get('expiration_date') is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Expiration date is required")
        if type(request.data.get('expiration_date')) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Expiration date must be a decimal string")
        if request.data.get('expiration_date').isdecimal() == False:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Expiration date must be a decimal string")
        expiration_date = int(request.data.get('expiration_date'))
        if not 1577847600000 <= expiration_date <= 3387133800000:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Expiration date must be between 2020-01-01 and 2077-05-01")
        if expiration_date <= creation_date:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Expiration date must be after creation date")
        
        if request.data.get('correct_answer') is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Correct answer is required")
        if type(request.data.get('correct_answer')) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Correct answer must be a string")
        
        exercise = self.usecase(
            exercise_id=request.data.get('exercise_id'),
            title=request.data.get('title'),
            enunciado=request.data.get('enunciado'),
            creation_date=creation_date,
            expiration_date=expiration_date,
            correct_answer=request.data.get('correct_answer')
        )
        
        viewmodel = CreateExerciseViewmodel(exercise)
        return Created(viewmodel.to_dict())