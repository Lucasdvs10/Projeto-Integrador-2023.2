from typing import Optional
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from src.shared.infra.dto.ExerciseMongoDTO import ExerciseMongoDTO
from src.shared.domain.repositories.exercise_repository_interface import IExerciseRepository
from src.shared.domain.entities.exercise import Exercise

load_dotenv()
env = os.environ

class ExerciseRepositoryMongo(IExerciseRepository):
    def __init__(self):
        self.mongo = MongoClient(env['MONGODB-URI'], server_api=ServerApi('1'))
        self.db = self.mongo[env['MONGODB-NAME']]
        self.collection = self.db[env['MONGODB-EXERCISE-COLLECTION']]
        
    def create_exercise(self, exercise: Exercise):
        item = ExerciseMongoDTO.from_entity(exercise).to_mongo()
        resp = self.collection.insert_one(item)
        
        return exercise
    
    def get_exercise_by_id(self, exercise_id: str):
        item = self.collection.find_one({"exercise_id": exercise_id})
        resp = None
        if item is not None:
            resp = ExerciseMongoDTO.from_mongo(item).to_entity()
        return resp
    
    def update_exercise_by_id(self, exercise_id: str, new_title: Optional[str] = None, new_enunciado: Optional[str] = None, new_creation_date: Optional[int] = None, new_expiration_date: Optional[int] = None, new_correct_answer: Optional[str] = None):
        updated_dict = {}
        if new_title is not None:
            updated_dict['title'] = new_title
        if new_enunciado is not None:
            updated_dict['enunciado'] = new_enunciado
        if new_creation_date is not None:
            updated_dict['creation_date'] = new_creation_date
        if new_expiration_date is not None:
            updated_dict['expiration_date'] = new_expiration_date
        if new_correct_answer is not None:
            updated_dict['correct_answer'] = new_correct_answer
            
        item = self.collection.find_one_and_update({"exercise_id": exercise_id}, {"$set": updated_dict}, return_document=True)
        
        return ExerciseMongoDTO.from_mongo(item).to_entity()
    
    def delete_exercise_by_id(self, exercise_id: str):
        item = self.collection.find_one({"exercise_id": exercise_id})
        self.collection.delete_one({"exercise_id": exercise_id})
        return ExerciseMongoDTO.from_mongo(item).to_entity()
    
    def get_all_exercises(self):
        items = self.collection.find()
        resp = None
        if items is not []:
            resp = [ExerciseMongoDTO.from_mongo(item).to_entity() for item in items]
        return resp
    
    def batch_create_exercises(self, exercises: list):
        items = [ExerciseMongoDTO.from_entity(exercise).to_mongo() for exercise in exercises]
        resp = self.collection.insert_many(items)
        return exercises