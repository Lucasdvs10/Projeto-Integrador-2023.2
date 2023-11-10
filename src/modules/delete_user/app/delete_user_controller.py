from .delete_user_usecase import DeleteUserUsecase
from .delete_user_viewmodel import DeleteUserViewmodel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from fastapi import HTTPException, status
from src.shared.domain.entities.user import User

from src.shared.helpers.external_interfaces.http_codes import OK

class DeleteUserController:
    def __init__(self, usecase: DeleteUserUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        if request.data.get("email") is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing email")
        if not User.validate_email(request.data.get("email")):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email")
        
        deleted_user = self.usecase(request.data.get("email"))
        viewmodel = DeleteUserViewmodel(deleted_user)
        return OK(viewmodel.to_dict())