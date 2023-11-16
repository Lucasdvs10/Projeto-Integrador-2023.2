from fastapi import HTTPException, status
from .delete_exercise_usecase import DeleteExerciseUsecase
from .delete_exercise_viewmodel import DeleteExerciseViewmodel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK


class DeleteExerciseController:
    def __init__(self, usecase: DeleteExerciseUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        exercise_id = request.data.get("exercise_id")
        if exercise_id is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing exercise id")
        if type(exercise_id) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Exercise id must be a string")
        
        exercise = self.usecase(exercise_id)
        viewmodel = DeleteExerciseViewmodel(exercise)
        return OK(viewmodel.to_dict())