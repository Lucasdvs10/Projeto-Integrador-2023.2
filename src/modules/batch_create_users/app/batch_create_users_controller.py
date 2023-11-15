from fastapi import HTTPException, status
from .batch_create_users_usecase import BatchCreateUsersUsecase
from .batch_create_users_viewmodel import BatchCreateUsersViewmodel
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import Created


class BatchCreateUsersController:
    def __init__(self, usecase: BatchCreateUsersUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        if not request.data.get("users") or len(request.data.get("users")) == 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Field users is missing")
        count = 1
        users = []
        for user in request.data.get("users"):
            if not user.get("EmailMaua"):
                if not user.get("RA"):
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Field EmailMaua (email) is missing in user " + str(count))
                request.data["users"][count - 1]["EmailMaua"] = str(user.get("RA")) + "@maua.br"
            if not user.get("Aluno"):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Field Aluno (name) is missing in user " + str(count))
            if not user.get("role"):
                request.data["users"][count - 1]["role"] = "STUDENT"
            if not user.get("password"):
                if not user.get("RG"):
                    request.data["users"][count - 1]["password"] = "SenhaPadrao123!"
                else:
                    request.data["users"][count - 1]["password"] = str(request.data["users"][count - 1]["RG"])
            if not User.validate_email(user.get("EmailMaua")):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid EmailMaua (email) in user " + str(count))
            if not User.validate_name(user.get("Aluno")):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Aluno (name) in user " + str(count))
            if user.get("role").upper() not in [role.value for role in ROLE]:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid role in user " + str(count))
            if not User.validate_password(user.get("password")):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password in user " + str(count))
            
            users.append(User(email=user.get("EmailMaua"), name=user.get("Aluno"), role=ROLE(user.get("role").upper()), password=user.get("password"), exercises_solved=[]))
            count += 1
            
        new_users = self.usecase(users=users)
        viewmodel = BatchCreateUsersViewmodel(new_users)
        return Created(viewmodel.to_dict())