from fastapi.exceptions import HTTPException
import pytest
from src.modules.validate_answer.app.validate_answer_usecase import ValidateAnswerUsecase
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ValidateAnswerUsecase:
    def test_validate_answer_usecase(self):
        answer_repository = AnswerRepositoryMock()
        user_repository = UserRepositoryMock()
        usecase = ValidateAnswerUsecase(answer_repository, user_repository)
        
        answer_id = answer_repository.all_answers[0].answer_id
        
        answer = usecase(answer_id)
        
        assert answer_repository.get_answer(answer_id).is_right == 1
        assert answer.exercise_id in user_repository.get_user_by_email(answer.email).exercises_solved 
        
    def test_validate_answer_usecase_answer_not_found(self):
        answer_repository = AnswerRepositoryMock()
        user_repository = UserRepositoryMock()
        usecase = ValidateAnswerUsecase(answer_repository, user_repository)
        
        answer_id = "999"
        
        with pytest.raises(HTTPException) as exc:
            usecase(answer_id)
        assert exc.value.status_code == 404
        assert exc.value.detail == "Answer not found"
        
    def test_validate_answer_usecase_user_not_found(self):
        answer_repository = AnswerRepositoryMock()
        user_repository = UserRepositoryMock()
        usecase = ValidateAnswerUsecase(answer_repository, user_repository)
        
        answer_id = answer_repository.all_answers[0].answer_id
        answer_repository.all_answers[0].email = "999"
        
        with pytest.raises(HTTPException) as exc:
            usecase(answer_id)
        assert exc.value.status_code == 404
        assert exc.value.detail == "User not found"