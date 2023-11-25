from .get_all_disciplines_usecase import GetAllDisciplinesUseCase
from .get_all_disciplines_viewmodel import GetAllDisciplinesViewmodel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK
from fastapi import HTTPException, status

class GetAllDisciplinesController:
    def __init__(self, usecase: GetAllDisciplinesUseCase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest = {}) -> IResponse:
        disciplines = self.usecase()
        viewmodel = GetAllDisciplinesViewmodel(disciplines)
    
        return OK(viewmodel.to_dict())