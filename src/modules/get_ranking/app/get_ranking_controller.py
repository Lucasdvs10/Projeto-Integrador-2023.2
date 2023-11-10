from src.shared.helpers.external_interfaces.external_interface import IRequest
from .get_ranking_usecase import GetRankingUsecase
from .get_ranking_viewmodel import GetRankingViewmodel
from src.shared.helpers.external_interfaces.http_codes import OK, InternalServerError


class GetRankingController:
    
    def __init__(self, usecase: GetRankingUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> dict:
        try:
            ranking = self.usecase()
            viewmodel = GetRankingViewmodel(ranking)
            return OK(viewmodel.to_dict())

        except Exception as err:
            return InternalServerError(body=err.args[0])