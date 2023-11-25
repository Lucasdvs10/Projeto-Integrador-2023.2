from src.shared.helpers.external_interfaces.http_codes import OK
from .delete_discipline_viewmodel import DeleteDisciplineViewmodel
from .delete_discipline_usecase import DeleteDisciplineUsecase
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from fastapi import HTTPException, status

class DeleteDisciplineController:
    def __init__(self, usecase: DeleteDisciplineUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        if request.data.get("discipline_id") is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing discipline_id")
        if type(request.data.get("discipline_id")) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid discipline_id")

        discipline = self.usecase(request.data.get("discipline_id"))
        viewmodel = DeleteDisciplineViewmodel(discipline)
        return OK(viewmodel.to_dict())