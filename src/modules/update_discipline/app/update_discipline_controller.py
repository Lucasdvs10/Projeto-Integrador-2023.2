from .update_discipline_viewmodel import UpdateDisciplineViewmodel
from .update_discipline_usecase import UpdateDisciplineUsecase
from src.shared.domain.entities.user import User
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK
from fastapi import HTTPException, status

class UpdateDisciplineController:
    def __init__(self, usecase: UpdateDisciplineUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        if not request.data.get("discipline_id"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing discipline_id")

        if "new_name" in request.data.keys():
            if not request.data.get("new_name"):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name can't be None")

            if type(request.data.get("new_name")) != str:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New name must be a string")

        if "new_year" in request.data.keys():
            if not request.data.get("new_year"):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Year can't be None")

            if type(request.data.get("new_year")) != int:
                if type(request.data.get("new_year")) != str:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New year must be an integer")
                if not request.data.get("new_year").isdigit():
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New year must be an integer")
                request.data["new_year"] = int(request.data.get("new_year"))
            if not 1 <= request.data.get("new_year") <= 6:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New year must be between 1 and 6")
            
        if "new_students_list" in request.data.keys():
            if not request.data.get("new_students_list"):
                request.data["new_students_list"] = []

            if type(request.data.get("new_students_list")) != list:
                if type(request.data.get("new_students_list")) != str:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New students list must be a list")
                if User.validate_email(request.data.get("new_students_list")):
                    request.data["new_students_list"] = [request.data.get("new_students_list")]

            for student in request.data.get("new_students_list"):
                if not User.validate_email(student):
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid email ({student})")
                
        response = self.usecase(discipline_id=request.data.get("discipline_id"), new_name=request.data.get("new_name"), new_year=request.data.get("new_year"), new_students_list=request.data.get("new_students_list"))
        
        viewmodel = UpdateDisciplineViewmodel(response)
        
        return OK(viewmodel.to_dict())