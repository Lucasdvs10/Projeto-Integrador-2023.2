from fastapi import HTTPException, status
from src.modules.get_answers.app.get_answers_usecase import GetAnswersUsecase
from src.modules.get_answers.app.get_answers_viewmodel import GetAnswersViewmodel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK


class GetAnswersController:
    def __init__(self, usecase: GetAnswersUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
      exercise_id = request.data.get("exercise_id")
      if exercise_id is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing exercise id")
      if type(exercise_id) != str:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Exercise id must be a string")
      answers = self.usecase(exercise_id)
      viewmodel = GetAnswersViewmodel(answers)
      return OK(viewmodel.to_dict())
        