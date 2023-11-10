import pytest

from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityParameterTypeError

class Test_User:
    def test_instantiate_user(self):
        user = User(email="22.01102-0@maua.br", name="João", role=ROLE.MONITOR, password="Teste123", exercises_solved=[])
        
        assert user
        
    def test_change_user_email(self):
        user = User(email="22.01102-0@maua.br", name="João", role=ROLE.MONITOR, password="Teste123", exercises_solved=[])
        
        user.email = "outroemail@maua.br"

        assert user.email == "outroemail@maua.br"
        
    def test_change_user_email_to_a_invalid_one(self):
        user = User(email="22.01102-0@maua.br", name="João", role=ROLE.MONITOR, password="Teste123", exercises_solved=[])
        
        with(pytest.raises(EntityParameterTypeError)):
            user.email = "outroemailmaua.br"
            
    def test_change_user_name(self):
        user = User(email="22.01102-0@maua.br", name="João", role=ROLE.MONITOR, password="Teste123", exercises_solved=[])
        
        user.name = "Outro nome"

        assert user.name == "Outro nome"
        
    def test_change_user_name_to_a_invalid_one(self):
        user = User(email="22.01102-0@maua.br", name="João", role=ROLE.MONITOR, password="Teste123", exercises_solved=[])
        
        with(pytest.raises(EntityParameterTypeError)):
            user.name = 42
            
    def test_change_user_role(self):
        user = User(email="22.01102-0@maua.br", name="João", role=ROLE.MONITOR, password="Teste123", exercises_solved=[])
        
        user.role = ROLE.STUDENT
        
        assert user.role == ROLE.STUDENT
        
    def test_change_user_role_to_a_invalid_one(self):
        user = User(email="22.01102-0@maua.br", name="João", role=ROLE.MONITOR, password="Teste123", exercises_solved=[])
        
        with(pytest.raises(EntityParameterTypeError)):
            user.role = "Monitor"
            
    def test_change_user_password(self):
        user = User(email="22.01102-0@maua.br", name="João", role=ROLE.MONITOR, password="Teste123", exercises_solved=[])
        
        user.password = "Outra senha"
        
        assert user.password == "Outra senha"
        
    def test_change_user_password_to_a_invalid_one(self):
        user = User(email="22.01102-0@maua.br", name="João", role=ROLE.MONITOR, password="Teste123", exercises_solved=[])
        
        with(pytest.raises(EntityParameterTypeError)):
            user.password = 42
            
    def test_change_user_exercises_solved_list(self):
        user = User(email="22.01102-0@maua.br", name="João", role=ROLE.MONITOR, password="Teste123", exercises_solved=[])
        
        user.exercises_solved = ["1", "2", "3"]
        
        assert user.exercises_solved == ["1", "2", "3"]
        
    def test_change_user_exercises_solved_list_to_a_invalid_one(self):
        user = User(email="22.01102-0@maua.br", name="João", role=ROLE.MONITOR, password="Teste123", exercises_solved=[])
        
        with(pytest.raises(EntityParameterTypeError)):
            user.exercises_solved = "Uma lista em string"