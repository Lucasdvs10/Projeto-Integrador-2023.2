from src.shared.domain.entities.user import User
from src.shared.domain.entities.answer import Answer
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.dto.UserMongoDTO import UserMongoDTO
from src.shared.infra.dto.AnswerMongoDTO import AnswerMongoDTO


class Test_AnswerMongoDTO:
    
    def test_answer_mongo_dto_from_entity(self):
        
        answer = Answer(
            answer_id="1",
            exercise_id="1",
            email="teste@gmail.com",
            content="teste",
            is_right=1
        )
        
        answer_mongo_dto = AnswerMongoDTO.from_entity(answer)
        
        
        assert answer_mongo_dto == AnswerMongoDTO(answer_id=answer.answer_id, exercise_id=answer.exercise_id, email=answer.email, content=answer.content, is_right=answer.is_right)
        
    def test_answer_mongo_dto_to_entity(self):
        answer_mongo_dto = AnswerMongoDTO(
            answer_id="1",
            exercise_id="1",
            email="teste@gmail.com",
            content="teste",
            is_right=1
        )
        
        answer = answer_mongo_dto.to_entity()
        
        assert answer == Answer(answer_id=answer_mongo_dto.answer_id, exercise_id=answer_mongo_dto.exercise_id, email=answer_mongo_dto.email, content=answer_mongo_dto.content, is_right=answer_mongo_dto.is_right)
        
    def test_answer_mongo_dto_to_mongo(self):
        answer_mongo_dto = AnswerMongoDTO(
            answer_id="1",
            exercise_id="1",
            email="teste@gmail.com",
            content="teste",
            is_right=1
        )
        
        answer = answer_mongo_dto.to_mongo()
        
        assert answer == {
            'answer_id': answer_mongo_dto.answer_id,
            'exercise_id': answer_mongo_dto.exercise_id,
            'email': answer_mongo_dto.email,
            'content': answer_mongo_dto.content,
            'is_right': answer_mongo_dto.is_right
        }
        
    def test_answer_mongo_dto_from_mongo(self):
        answer = {
            'answer_id': "1",
            'exercise_id': "1",
            'email': "teste@gmail.com",
            'content': "teste",
            'is_right': 1
        }
        
        answer_mongo_dto = AnswerMongoDTO.from_mongo(answer)
        
        assert answer_mongo_dto == AnswerMongoDTO(answer_id=answer['answer_id'], exercise_id=answer['exercise_id'], email=answer['email'], content=answer['content'], is_right=answer['is_right'])