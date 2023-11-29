from typing import List, Optional
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from src.shared.infra.dto.AnswerMongoDTO import UserMongoDTO
from dotenv import load_dotenv

load_dotenv()
env = os.environ


class UserRepositoryMongo(IUserRepository):
    def __init__(self):
        self.mongo = MongoClient(env['MONGODB-URI'], server_api=ServerApi('1'))
        self.db = self.mongo[env['MONGODB-NAME']]
        self.collection = self.db[env['MONGODB-USER-COLLECTION']]
        
    def create_user(self, user: User):
        item = UserMongoDTO.from_entity(user).to_mongo()
        resp = self.collection.insert_one(item)
        
        return user
    
    def get_user_by_email(self, email: str):
        item = self.collection.find_one({"email": email})
        resp = None
        if item is not None:
            resp = UserMongoDTO.from_mongo(item).to_entity()
        return resp
    
    def update_user_by_email(self, email: str, new_name: Optional[str] = None, new_role: Optional[str] = None, new_password: Optional[str] = None, new_exercises_solved: Optional[List[str]] = None):
        updated_dict = {}
        if new_name is not None:
            updated_dict['name'] = new_name
        if new_role is not None:
            updated_dict['role'] = new_role
        if new_password is not None:
            updated_dict['password'] = new_password
        if new_exercises_solved is not None:
            updated_dict['exercises_solved'] = new_exercises_solved
            
        item = self.collection.find_one_and_update({"email": email}, {"$set": updated_dict}, return_document=True)
        
        return UserMongoDTO.from_mongo(item).to_entity()
    
    def delete_user_by_email(self, email: str):
        item = self.collection.find_one({"email": email})
        self.collection.delete_one({"email": email})
        return UserMongoDTO.from_mongo(item).to_entity()
    
    def get_all_users(self):
        items = self.collection.find()
        resp = None
        if items is not []:
            resp = [UserMongoDTO.from_mongo(item).to_entity() for item in items]
        return resp
    
    def batch_create_users(self, users: list):
        items = [UserMongoDTO.from_entity(user).to_mongo() for user in users]
        resp = self.collection.insert_many(items)
        
        return users