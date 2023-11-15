from fastapi import HTTPException, status
from src.modules.create_user.app.create_user_viewmodel import CreateUserViewmodel
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.external_interfaces.external_interface import IRequest
from src.shared.helpers.external_interfaces.http_codes import Created
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from .create_user_usecase import CreateUserUsecase


class CreateUserController:
    def __init__(self, usecase: CreateUserUsecase):
        self.usecase = usecase
        
    def __call__(self, request: HttpRequest) -> HttpResponse:
        if not request.data.get("email"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Field email is missing")
        if not User.validate_email(request.data.get("email")):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email")
        
        if not request.data.get("name"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Field name is missing")
        if not User.validate_name(request.data.get("name")):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid name")
    
        if not request.data.get("role"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Field role is missing")
        if type(request.data.get("role")) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid role")        
        if request.data.get("role").upper() not in [role.value for role in ROLE]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid role")
        role = ROLE(request.data.get("role").upper())
    
        
        if not request.data.get("password"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Field password is missing")
        if not User.validate_password(request.data.get("password")):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password")
        
        new_user = self.usecase(email=request.data.get("email"), name=request.data.get("name"), role=role, password=request.data.get("password"))
        
        viewmodel = CreateUserViewmodel(new_user)
        return Created(viewmodel.to_dict())