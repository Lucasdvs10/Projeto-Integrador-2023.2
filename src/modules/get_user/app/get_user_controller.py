from fastapi import HTTPException, status
from src.modules.get_user.app.get_user_usecase import GetUserUsecase
from src.modules.get_user.app.get_user_viewmodel import GetUserViewmodel
from src.shared.domain.entities.user import User
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK


class GetUserController:
    def __init__(self, usecase: GetUserUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        email = request.data.get("email")
        
        if not email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing email")
        if not User.validate_email(email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email")
        
        user = self.usecase(email=email)
        viewmodel = GetUserViewmodel(user)
        
        return OK(viewmodel.to_dict())