import copy
from src.modules.update_answer.app.update_answer_usecase import UpdateAnswerUsecase
from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock
from fastapi import HTTPException
import pytest

class Test_UpdateAnswerUsecase:
    def test_update_answer_usecase(self):
        repo = AnswerRepositoryMock()
        usecase = UpdateAnswerUsecase(repo)
        answer_id = repo.all_answers[0].answer_id
        old_answer = copy.deepcopy(repo.get_answer(answer_id))        

        updated_answer = usecase(answer_id, "New content", "New email", 1)
        
        assert old_answer != updated_answer
        assert repo.get_answer(answer_id) == updated_answer
        
    def test_update_answer_usecase_with_nonexistent_answer(self):
        repo = AnswerRepositoryMock()
        usecase = UpdateAnswerUsecase(repo)
        answer_id = "notfound"
        
        with pytest.raises(HTTPException) as exc:
            usecase(answer_id, "New content", "New email", 1)
        assert exc.value.status_code == 404
        assert exc.value.detail == "Answer not found"