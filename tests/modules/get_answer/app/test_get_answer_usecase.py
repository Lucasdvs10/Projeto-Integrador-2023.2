import pytest
from src.modules.get_answer.app.get_answer_usecase import GetAnswerUsecase
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock
from fastapi import HTTPException

class Test_GetAnswerUsecase:
    def test_get_answer_usecase(self):
        repo = AnswerRepositoryMock()
        usecase = GetAnswerUsecase(repo)
        answer = usecase(repo.all_answers[0].answer_id)
        assert answer == repo.all_answers[0]
        
    def test_get_answer_usecase_not_found(self):
        repo = AnswerRepositoryMock()
        usecase = GetAnswerUsecase(repo)
        
        with pytest.raises(HTTPException) as exc:
            usecase("not_found")
        assert exc.value.status_code == 404
        assert exc.value.detail == "Answer not found"