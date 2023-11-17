from .get_all_disciplines_usecase import GetAllDisciplinesUseCase
from .get_all_disciplines_viewmodel import GetAllDisciplinesViewmodel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK
from fastapi import HTTPException, status

class GetAllDisciplinesController:
    def __init__(self, usecase: GetAllDisciplinesUseCase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest = {}) -> IResponse:
        try:
            disciplines = self.usecase()
            viewmodel = GetAllDisciplinesViewmodel(disciplines)
        
            return OK(viewmodel.to_dict())
    
        except Exception as exc:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc))