from .create_discipline_usecase import CreateDisciplineUsecase
from .create_discipline_viewmodel import CreateDisciplineViewmodel
from src.shared.domain.entities.user import User
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from fastapi import HTTPException, status

from src.shared.helpers.external_interfaces.http_codes import Created

class CreateDisciplineController:
    def __init__(self, usecase: CreateDisciplineUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        if not request.data.get("name"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing name")
        if type(request.data["name"]) != str:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid name")
        
        if not request.data.get("year"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing year")
        if type(request.data["year"]) != int:
            if type(request.data["year"]) != str:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid year")
            if not request.data["year"].isdigit():
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid year")
            request.data["year"] = int(request.data["year"])

        if not request.data.get("students_emails_list"):
            request.data["students_emails_list"] = []
        if type(request.data["students_emails_list"]) != list:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid students_emails_list")
        for email in request.data["students_emails_list"]:
            if not User.validate_email(email):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid email ({email})")
        
            
        response = self.usecase(
            name=request.data["name"],
            year=request.data["year"],
            students_emails_list=request.data["students_emails_list"]
        )
        
        viewmodel = CreateDisciplineViewmodel(response)
        return Created(viewmodel.to_dict())