from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.external_interfaces.http_codes import OK
from .update_user_viewmodel import UpdateUserViewmodel
from .update_user_usecase import UpdateUserUsecase
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from fastapi import HTTPException, status

class UpdateUserController:
    def __init__(self, usecase: UpdateUserUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        if request.data.get("email") is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing email")
        
        if not User.validate_email(request.data.get("email")):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email")
        
        if 'new_name' in request.data.keys():
            if request.data.get("new_name") is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name can't be None")
            
            if not User.validate_name(request.data.get("new_name")):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid new name")
        
        new_role = None
        if 'new_role' in request.data.keys():
            if request.data.get("new_role") is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Role can't be None")
            
            if request.data.get("new_role").upper() not in [role.value for role in ROLE]:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid role")
                    
            new_role = ROLE(request.data.get("new_role").upper())
        
        if 'new_password' in request.data.keys():
            if request.data.get("new_password") is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password can't be None")
            
            if not User.validate_password(request.data.get("new_password")):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid new password")
        
        new_exercises_solved = None
        if 'new_exercises_solved' in request.data.keys():
            new_exercises_solved = []
            if request.data.get("new_exercises_solved") is not None:
                if type(request.data.get("new_exercises_solved")) != list:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid new exercises solved")

                if not all(type(exercise_id) == str for exercise_id in request.data.get("new_exercises_solved")):
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid new exercises solved")
                
                new_exercises_solved = request.data.get("new_exercises_solved")
                
        updated_user = self.usecase(email=request.data.get("email"), new_name=request.data.get("new_name"), new_role=new_role, new_password=request.data.get("new_password"), new_exercises_solved=new_exercises_solved)
        
        viewmodel = UpdateUserViewmodel(updated_user)

        return OK(viewmodel.to_dict())