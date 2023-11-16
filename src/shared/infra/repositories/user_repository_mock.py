from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.domain.entities.user import User
from typing import Optional


class UserRepositoryMock(IUserRepository):
    def __init__(self):
        self._users = [
            User(
                email="22.28764-1@maua.br",
                name="Jeremy Sanders",
                role=ROLE.MONITOR,
                password="UJDC3Gu0",
                exercises_solved=[],
            ),
            User(
                email="10.22533-7@maua.br",
                name="Doris Williams",
                role=ROLE.STUDENT,
                password="1XHMHUIH",
                exercises_solved=[],
            ),
            User(
                email="22.39800-8@maua.br",
                name="Alma Gil",
                role=ROLE.TEACHER,
                password="FMAXZzol",
                exercises_solved=[],
            ),
            User(
                email="15.20620-3@maua.br",
                name="Beverly Mccabe",
                role=ROLE.MONITOR,
                password="N4suwDhN",
                exercises_solved=[],
            ),
            User(
                email="23.38161-5@maua.br",
                name="Thomas Ownbey",
                role=ROLE.TEACHER,
                password="ZOffefI5",
                exercises_solved=[],
            ),
            User(
                email="22.35652-0@maua.br",
                name="Scott Beachy",
                role=ROLE.ADMIN,
                password="dFtTHIpu",
                exercises_solved=[],
            ),
            User(
                email="21.21862-1@maua.br",
                name="Tammy Estep",
                role=ROLE.TEACHER,
                password="igNMC87b",
                exercises_solved=[],
            ),
            User(
                email="13.28677-0@maua.br",
                name="Tonda Fuller",
                role=ROLE.TEACHER,
                password="lvlXSGKn",
                exercises_solved=[],
            ),
            User(
                email="18.36021-2@maua.br",
                name="Carolyn Caron",
                role=ROLE.MONITOR,
                password="ZN2OrM2k",
                exercises_solved=[],
            ),
            User(
                email="17.32602-8@maua.br",
                name="Jeanette Jones",
                role=ROLE.ADMIN,
                password="5iB36x2N",
                exercises_solved=[],
            ),
            User(
                email="19.27403-0@maua.br",
                name="John Burden",
                role=ROLE.MONITOR,
                password="9hy77c6U",
                exercises_solved=[],
            ),
            User(
                email="17.33773-1@maua.br",
                name="Levi Jimenez",
                role=ROLE.ADMIN,
                password="uLQyaijn",
                exercises_solved=[],
            ),
            User(
                email="21.37594-4@maua.br",
                name="David Davis",
                role=ROLE.STUDENT,
                password="5o9hhfCZ",
                exercises_solved=[],
            ),
            User(
                email="10.25184-4@maua.br",
                name="Kelvin Hill",
                role=ROLE.ADMIN,
                password="LtcAsAFS",
                exercises_solved=[],
            ),
            User(
                email="17.23039-7@maua.br",
                name="John Woo",
                role=ROLE.MONITOR,
                password="4x2qdmJ8",
                exercises_solved=[],
            ),
            User(
                email="22.23688-2@maua.br",
                name="Stephanie Thompson",
                role=ROLE.TEACHER,
                password="GRXJsLOd",
                exercises_solved=[],
            ),
            User(
                email="11.35709-7@maua.br",
                name="Michele Green",
                role=ROLE.STUDENT,
                password="wCMtcIlB",
                exercises_solved=[],
            ),
            User(
                email="15.26374-2@maua.br",
                name="Anna Ethington",
                role=ROLE.STUDENT,
                password="QgdVdxaM",
                exercises_solved=[],
            ),
            User(
                email="23.25802-7@maua.br",
                name="Soon Kelsey",
                role=ROLE.TEACHER,
                password="MZhyLM9k",
                exercises_solved=[],
            ),
            User(
                email="20.35261-5@maua.br",
                name="James Matthewson",
                role=ROLE.TEACHER,
                password="pNMJJuPH",
                exercises_solved=[],
            ),
            User(
                email="15.35670-9@maua.br",
                name="Rena Waguespack",
                role=ROLE.ADMIN,
                password="iTCw0rMW",
                exercises_solved=[],
            ),
            User(
                email="17.25662-2@maua.br",
                name="Ken Sparkman",
                role=ROLE.ADMIN,
                password="yixIBj8U",
                exercises_solved=[],
            ),
            User(
                email="21.27492-7@maua.br",
                name="Eva Troublefield",
                role=ROLE.STUDENT,
                password="sPLpWhKE",
                exercises_solved=[],
            ),
            User(
                email="19.34257-4@maua.br",
                name="Renee Lewis",
                role=ROLE.TEACHER,
                password="XGqLLLK4",
                exercises_solved=[],
            ),
            User(
                email="14.25099-0@maua.br",
                name="Richard Villegas",
                role=ROLE.ADMIN,
                password="aS8FU3Ke",
                exercises_solved=[],
            ),
            User(
                email="11.28995-6@maua.br",
                name="Sylvia Mann",
                role=ROLE.TEACHER,
                password="twuJGVeg",
                exercises_solved=[],
            ),
            User(
                email="23.30866-8@maua.br",
                name="Anthony Mccormick",
                role=ROLE.MONITOR,
                password="Sn2BIWu1",
                exercises_solved=[],
            ),
            User(
                email="13.38661-3@maua.br",
                name="Allen Avans",
                role=ROLE.STUDENT,
                password="XlWSAYgx",
                exercises_solved=[],
            ),
            User(
                email="21.31651-4@maua.br",
                name="Adele Springer",
                role=ROLE.STUDENT,
                password="0erH0X35",
                exercises_solved=[],
            ),
            User(
                email="20.38976-0@maua.br",
                name="Delores King",
                role=ROLE.MONITOR,
                password="iXvidVvm",
                exercises_solved=[],
            ),
            User(
                email="21.22789-4@maua.br",
                name="Joseph Zane",
                role=ROLE.TEACHER,
                password="3MOapRdn",
                exercises_solved=[],
            ),
            User(
                email="17.24327-1@maua.br",
                name="Dean Coelho",
                role=ROLE.MONITOR,
                password="Twb5Zaqp",
                exercises_solved=[],
            ),
            User(
                email="16.38514-6@maua.br",
                name="Jason Moore",
                role=ROLE.STUDENT,
                password="jRKWzYN8",
                exercises_solved=[],
            ),
            User(
                email="11.33959-6@maua.br",
                name="Xiomara Forbes",
                role=ROLE.TEACHER,
                password="TgHyIckJ",
                exercises_solved=[],
            ),
            User(
                email="23.30094-4@maua.br",
                name="Robert Horton",
                role=ROLE.ADMIN,
                password="8aenk6v7",
                exercises_solved=[],
            ),
            User(
                email="20.29939-4@maua.br",
                name="Herman Clayton",
                role=ROLE.MONITOR,
                password="cAIkyGYL",
                exercises_solved=[],
            ),
            User(
                email="20.36742-8@maua.br",
                name="Michael Cauthen",
                role=ROLE.STUDENT,
                password="m9P7dpFj",
                exercises_solved=[],
            ),
            User(
                email="13.23344-4@maua.br",
                name="Mary Lutz",
                role=ROLE.TEACHER,
                password="WSvrKLU7",
                exercises_solved=[],
            ),
            User(
                email="12.30190-8@maua.br",
                name="Robert Lugo",
                role=ROLE.ADMIN,
                password="CdFCkKcQ",
                exercises_solved=[],
            ),
            User(
                email="17.35107-3@maua.br",
                name="John Daniels",
                role=ROLE.MONITOR,
                password="grLwfgjB",
                exercises_solved=[],
            ),
            User(
                email="22.28060-3@maua.br",
                name="Miguel Hernandez",
                role=ROLE.STUDENT,
                password="WukxnJ3K",
                exercises_solved=[],
            ),
            User(
                email="14.27213-8@maua.br",
                name="Wendy Davis",
                role=ROLE.ADMIN,
                password="lFF5U02C",
                exercises_solved=[],
            ),
            User(
                email="22.20806-3@maua.br",
                name="Charlotte Duncan",
                role=ROLE.MONITOR,
                password="rx5sNfoI",
                exercises_solved=[],
            ),
            User(
                email="15.33674-2@maua.br",
                name="Adrian Sisk",
                role=ROLE.STUDENT,
                password="LCIYFWG7",
                exercises_solved=[],
            ),
            User(
                email="20.20157-5@maua.br",
                name="Emma Heald",
                role=ROLE.STUDENT,
                password="SMetwsJx",
                exercises_solved=[],
            ),
            User(
                email="13.38997-2@maua.br",
                name="Thelma Scheele",
                role=ROLE.STUDENT,
                password="je4lrkob",
                exercises_solved=[],
            ),
            User(
                email="19.23349-2@maua.br",
                name="Chan Salazar",
                role=ROLE.TEACHER,
                password="Ssy4LJzn",
                exercises_solved=[],
            ),
            User(
                email="19.33471-0@maua.br",
                name="Rosa Cooley",
                role=ROLE.TEACHER,
                password="yJHPHnYy",
                exercises_solved=[],
            ),
            User(
                email="21.31950-7@maua.br",
                name="Helen Rose",
                role=ROLE.TEACHER,
                password="CruhLoFK",
                exercises_solved=[],
            ),
            User(
                email="20.31440-7@maua.br",
                name="Charles Young",
                role=ROLE.ADMIN,
                password="fwERHX3L",
                exercises_solved=[],
            ),
            User(
                email="22.01102-0@maua.br",
                name="Luigi Trevisan",
                role=ROLE.MONITOR,
                password="ebdf496f67651cddf6aaa1f0b130f1b99ce9e2e93dc2503d926edcff15aee668",
                exercises_solved=[],
            ),
            User(
                email="22.01049-0@maua.br",
                name="Vitor Negresiolo",
                role=ROLE.STUDENT,
                password="ebdf496f67651cddf6aaa1f0b130f1b99ce9e2e93dc2503d926edcff15aee668",
                exercises_solved=[1, 2, 3],
            ),
            User(
                email="22.00680-0@maua.br",
                name="Rodrigo Siqueira",
                role=ROLE.STUDENT,
                password="ebdf496f67651cddf6aaa1f0b130f1b99ce9e2e93dc2503d926edcff15aee668",
                exercises_solved=[1, 2],
            ),
        ]

    def create_user(self, user: User):
        self._users.append(user)
        return user

    def update_user_by_email(
        self,
        email: str,
        new_name: Optional[str] = None,
        new_role: Optional[str] = None,
        new_password: Optional[str] = None,
        new_exercises_solved: Optional[list] = None,
    ):
        user = self.get_user_by_email(email)

        if user is None:
            return None

        if new_name:
            user.name = new_name
        if new_role:
            user.role = new_role
        if new_password:
            user.password = new_password
        if new_exercises_solved:
            user.exercises_solved = new_exercises_solved

        return user

    def get_user_by_email(self, email: str):
        for user in self._users:
            if user.email == email:
                return user
        return None

    def delete_user_by_email(self, email: str):
        user = self.get_user_by_email(email)
        self._users.remove(user)
        return user

    def get_all_users(self):
        return self._users

    def batch_create_users(self, users: list):
        for user in users:
            self._users.append(user)
        return users