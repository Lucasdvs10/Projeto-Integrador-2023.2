from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.dto.UserMongoDTO import UserMongoDTO


class Test_UserMongoDTO:
    
    def test_user_mongo_dto_from_entity(self):
        user = User(
            email="22.01102-0@maua.br",
            name="Luigi Trevisan",
            exercises_solved=[],
            password="Senha123!",
            role=ROLE.MONITOR
        )
        
        user_mongo_dto = UserMongoDTO.from_entity(user)
        
        assert user_mongo_dto == UserMongoDTO(email=user.email, name=user.name, role=user.role, password=user.password, exercises_solved=user.exercises_solved)
        
    def test_user_mongo_dto_to_entity(self):
        user_mongo_dto = UserMongoDTO(
            email="22.01102-0@maua.br",
            name="Luigi Trevisan",
            exercises_solved=[],
            password="Senha123!",
            role=ROLE.MONITOR
        )
        
        user = user_mongo_dto.to_entity()
        
        assert user == User(email=user_mongo_dto.email, name=user_mongo_dto.name, role=user_mongo_dto.role, password=user_mongo_dto.password, exercises_solved=user_mongo_dto.exercises_solved)
        
    def test_user_mongo_dto_to_mongo(self):
        user_mongo_dto = UserMongoDTO(
            email="22.01102-0@maua.br",
            name="Luigi Trevisan",
            exercises_solved=[],
            password="Senha123!",
            role=ROLE.MONITOR
        )
        
        user = user_mongo_dto.to_mongo()
        
        assert user == {
            'email': user_mongo_dto.email,
            'name': user_mongo_dto.name,
            'role': user_mongo_dto.role.value,
            'password': user_mongo_dto.password,
            'exercises_solved': user_mongo_dto.exercises_solved
        }
        
    def test_user_mongo_dto_from_mongo(self):
        user = {
            'email': "22.01102-0@maua.br",
            'name': "Luigi Trevisan",
            'role': ROLE.MONITOR.value,
            'password': "Senha123!",
            'exercises_solved': []
        }
        
        user_mongo_dto = UserMongoDTO.from_mongo(user)
        
        assert user_mongo_dto == UserMongoDTO(email=user['email'], name=user['name'], role=ROLE(user['role']), password=user['password'], exercises_solved=user['exercises_solved'])