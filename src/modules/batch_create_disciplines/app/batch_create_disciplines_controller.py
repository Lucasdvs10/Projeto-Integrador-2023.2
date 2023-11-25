import uuid

from src.shared.domain.entities.user import User
from .batch_create_disciplines_viewmodel import BatchCreateDisciplinesViewmodel
from src.shared.domain.entities.discipline import Discipline
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from .batch_create_disciplines_usecase import BatchCreateDisciplinesUseCase
from fastapi import HTTPException, status
from src.shared.helpers.external_interfaces.http_codes import Created

class BatchCreateDisciplinesController:
    def __init__(self, usecase: BatchCreateDisciplinesUseCase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        if not request.data.get("disciplines") or type(request.data.get("disciplines")) != list or len(request.data.get("disciplines")) == 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Field disciplines is missing")
        count = 1
        disciplines = []
        for discipline in request.data.get("disciplines"):
            if not discipline.get("name"):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Field name is missing in discipline " + str(count))
            
            if not discipline.get("discipline_id"):
                discipline["discipline_id"] = str(uuid.uuid4())
                
            if not discipline.get("year"):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Field year is missing in discipline " + str(count))
            
            if not discipline.get("students_emails_list"):
                discipline["students_emails_list"] = []
                
            if type(discipline.get("name")) is not str:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid name in discipline " + str(count))
            
            if type(discipline.get("discipline_id")) is not str:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid discipline_id in discipline " + str(count))
            
            if type(discipline.get("year")) is not int:
                if type(discipline.get("year")) is not str:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid year in discipline " + str(count))
                if not discipline.get("year").isdigit():
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid year in discipline " + str(count))
                discipline["year"] = int(discipline["year"])
            
            if type(discipline.get("students_emails_list")) is not list:
                if type(discipline.get("students_emails_list")) is not str:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid students_emails_list in discipline " + str(count))
                if User.validate_email(discipline.get("students_emails_list")):
                    discipline["students_emails_list"] = [discipline.get("students_emails_list")]
                if discipline.get("students_emails_list")[0] == "[" and discipline.get("students_emails_list")[-1] == "]":
                    discipline["students_emails_list"] = discipline.get("students_emails_list")[1:-1].split(",")
                else:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid students_emails_list in discipline " + str(count))
                
            
            for email in discipline.get("students_emails_list"):
                if email is None:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email " + email + " in discipline " + str(count))
                if not User.validate_email(email):
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email " + email + " in discipline " + str(count))

            disciplines.append(Discipline(
                name=discipline.get("name"),
                discipline_id=discipline.get("discipline_id"),
                year=discipline.get("year"),
                students_emails_list=discipline.get("students_emails_list")
            ))
            count += 1
            
        new_disciplines = self.usecase(disciplines=disciplines)
        viewmodel = BatchCreateDisciplinesViewmodel(new_disciplines)
        return Created(viewmodel.to_dict())