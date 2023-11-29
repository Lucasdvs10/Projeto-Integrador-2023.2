from enum import Enum
import os
from src.shared.domain.repositories.answer_repository_interface import IAnswerRepository
from src.shared.domain.repositories.exercise_repository_interface import IExerciseRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository


class STAGE(Enum):
    DOTENV = "DOTENV"
    DEV = "DEV"
    HOMOLOG = "HOMOLOG"
    PROD = "PROD"
    TEST = "TEST"


class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

    Usage:

    """
    stage: STAGE
    uri: str
    db_name: str
    user_collection: str
    discipline_collection: str
    exercise_collection: str
    answer_collection: str
    schedule_collection: str

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv()
        os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.DOTENV.value

    def load_envs(self):
        if "STAGE" not in os.environ or os.environ["STAGE"] == STAGE.DOTENV.value:
            self._configure_local()

        self.stage = STAGE[os.environ.get("STAGE")]
        
        if self.stage == STAGE.TEST:
            self.uri = "mongodb://localhost:27017"
            self.db_name = "monitoria"
            self.user_collection = "users"
            self.discipline_collection = "disciplines"
            self.exercise_collection = "exercises"
            self.answer_collection = "answers"
            self.schedule_collection = "schedules"

        else:
            self.uri = os.environ.get("MONGODB-URI")
            self.db_name = os.environ.get("MONGODB-NAME") if os.environ.get("MONGODB-NAME") else "monitoria"
            self.user_collection = os.environ.get("MONGODB-USER-COLLECTION") if os.environ.get("MONGODB-USER-COLLECTION") else "users"
            self.discipline_collection = os.environ.get("MONGODB-DISCIPLINE-COLLECTION") if os.environ.get("MONGODB-DISCIPLINE-COLLECTION") else "disciplines"
            self.exercise_collection = os.environ.get("MONGODB-EXERCISE-COLLECTION") if os.environ.get("MONGODB-EXERCISE-COLLECTION") else "exercises"
            self.answer_collection = os.environ.get("MONGODB-ANSWER-COLLECTION") if os.environ.get("MONGODB-ANSWER-COLLECTION") else "answers"
            self.schedule_collection = os.environ.get("MONGODB-SCHEDULE-COLLECTION") if os.environ.get("MONGODB-SCHEDULE-COLLECTION") else "schedules"

    @staticmethod
    def get_user_repo() -> IUserRepository:
        if Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from src.shared.infra.repositories.user_repository_mongo import UserRepositoryMongo
            return UserRepositoryMongo
        from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
        return UserRepositoryMock
    
    @staticmethod
    def get_answer_repo() -> IAnswerRepository:
        if Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from src.shared.infra.repositories.answer_repository_mongo import AnswerRepositoryMongo
            return AnswerRepositoryMongo
        from src.shared.infra.repositories.answer_repository_mock import AnswerRepositoryMock
        return AnswerRepositoryMock
    
    @staticmethod
    def get_exercise_repo() -> IExerciseRepository:
        if Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from src.shared.infra.repositories.exercise_repository_mongo import ExerciseRepositoryMongo
            return ExerciseRepositoryMongo
        from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock
        return ExerciseRepositoryMock
        
    @staticmethod
    def get_envs() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        :return: Environments (stage={self.stage}, s3_bucket_name={self.s3_bucket_name}, region={self.region}, endpoint_url={self.endpoint_url})

        """
        envs = Environments()
        envs.load_envs()
        return envs

    def __repr__(self):
        return self.__dict__

