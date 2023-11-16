from fastapi import HTTPException, status
from .get_exercise_usecase import GetExerciseUsecase
from .get_exercise_viewmodel import GetExerciseViewmodel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK


class GetExerciseController:
    def __init__(self, usecase: GetExerciseUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        exercise_id = request.data.get("exercise_id")
        if exercise_id is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing exercise id")
        if type(exercise_id) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Exercise id must be a string")
        
        exercise = self.usecase(exercise_id)
        viewmodel = GetExerciseViewmodel(exercise)
        return OK(viewmodel.to_dict())