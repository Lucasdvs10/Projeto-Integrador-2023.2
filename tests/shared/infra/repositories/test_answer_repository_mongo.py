import pytest
from src.shared.domain.entities.answer import Answer
from src.shared.domain.entities.schedule import Schedule
from src.shared.infra.repositories.answer_repository_mongo import AnswerRepositoryMongo


class Test_AnswerRepositoryMongo:
    @pytest.mark.skip(reason="MongoDB is not available")
    def test_create_answer(self):
        repo = AnswerRepositoryMongo()
        new_answer = Answer(answer_id="1", exercise_id="1", email="22.01102-0@maua.br", content="Teste", is_right=0)
        
        response = repo.create_answer(new_answer)
        assert type(response) == Answer
        assert repo.get_answer(answer_id=new_answer.answer_id) == new_answer
        
    @pytest.mark.skip(reason="MongoDB is not available")
    def test_get_answer(self):
        repo = AnswerRepositoryMongo()
        answer_id = "1"
        answer = repo.get_answer(answer_id=answer_id)
        
        assert type(answer) == Answer
        assert answer.answer_id == answer_id
        
    @pytest.mark.skip(reason="MongoDB is not available")
    def test_update_answer(self):
        repo = AnswerRepositoryMongo()
        answer_id = "1"
        new_answer = repo.update_answer(answer_id=answer_id, new_content="Atualizado", new_email="21.01049-0@maua.br", new_is_right=1)
        
        assert type(new_answer) == Answer
        assert new_answer.answer_id == answer_id
        assert new_answer.content == "Atualizado"
        
    @pytest.mark.skip(reason="MongoDB is not available")
    def test_delete_answer(self):
        repo = AnswerRepositoryMongo()
        answer_id = "1"
        answer = repo.delete_answer(answer_id=answer_id)
        
        assert type(answer) == Answer
        assert answer.answer_id == answer_id
        assert repo.get_answer(answer_id=answer_id) == None
        
    @pytest.mark.skip(reason="MongoDB is not available")
    def test_get_answers(self):
        repo = AnswerRepositoryMongo()
        answers = repo.get_answers(exercise_id="1")
        
        assert type(answers) == list

    @pytest.mark.skip(reason="MongoDB is not available")
    def test_get_schedule(self):
        repo = AnswerRepositoryMongo()
        schedule = repo.get_schedule()

        assert type(schedule) == Schedule
        
    @pytest.mark.skip(reason="MongoDB is not available")
    def test_update_schedule(self):
        repo = AnswerRepositoryMongo()
        new_schedule = repo.update_schedule(new_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        
        assert type(new_schedule) == Schedule
        assert new_schedule.url == "https://www.youtube.com/watch?v=dQw4w9WgXcQ"