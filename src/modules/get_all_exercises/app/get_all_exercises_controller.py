from .get_all_exercises_usecase import GetAllExercisesUsecase
from .get_all_exercises_viewmodel import GetAllExercisesViewmodel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK
from fastapi import HTTPException, status

class GetAllExercisesController:
    def __init__(self, usecase: GetAllExercisesUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest = {}) -> IResponse:
        try:
            exercises = self.usecase()
            viewmodel = GetAllExercisesViewmodel(exercises)
        
            return OK(viewmodel.to_dict())
    
        except Exception as exc:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc))