import os
from typing import Optional
from pymongo import MongoClient
from src.shared.domain.entities.answer import Answer
from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.answer_repository_interface import IAnswerRepository
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

from src.shared.infra.dto.AnswerMongoDTO import AnswerMongoDTO

load_dotenv()
env = os.environ


class AnswerRepositoryMongo(IAnswerRepository):
  def __init__(self):
    self.mongo = MongoClient(env['MONGODB-URI'], server_api=ServerApi('1'))
    self.db = self.mongo[env['MONGODB-NAME']]
    self.collection = self.db[env['MONGODB-ANSWER-COLLECTION']]
    self.collection_schedule = self.db[env['MONGODB-SCHEDULE-COLLECTION']]
    
  
  def create_answer(self, answer: Answer):
    item = AnswerMongoDTO.from_entity(answer).to_mongo()
    self.collection.insert_one(item)
    
    return answer
  
  def get_answers(self, exercise_id: str):
    items = self.collection.find({"exercise_id": exercise_id})
    resp = None
    if items is not None:
      resp = [AnswerMongoDTO.from_mongo(item).to_entity() for item in items]
    return resp
  
  def get_answer(self, answer_id: str) -> Answer:
    item = self.collection.find_one({"_id": answer_id})
    resp = None
    if item is not None:
      resp = AnswerMongoDTO.from_mongo(item).to_entity()
    return resp
  
  def update_answer(self, answer_id: str, new_content: Optional[str] = None, new_is_right: Optional[bool] = None):
    updated_dict = {}
    if new_content is not None:
      updated_dict['content'] = new_content
    if new_is_right is not None:
      updated_dict['is_right'] = new_is_right
      
    item = self.collection.find_one_and_update({"_id": answer_id}, {"$set": updated_dict}, return_document=True)
    
    return AnswerMongoDTO.from_mongo(item).to_entity()
  
  def delete_answer(self, answer_id: str) -> Answer:
    item = self.collection.find_one({"_id": answer_id})
    self.collection.delete_one({"_id": answer_id})
    return AnswerMongoDTO.from_mongo(item).to_entity()
  
  def get_schedule(self) -> Schedule:
    item = self.collection_schedule.find()
    resp = None
    if item is not None:
      resp = Schedule.from_mongo(item)
    return resp
  
  def update_schedule(self, new_url: str) -> Schedule:
    updated_dict = {}
    if new_url is not None:
      updated_dict['url'] = new_url
      
    item = self.collection_schedule.find_one_and_update({}, {"$set": updated_dict}, return_document=True)
    
    return Schedule.from_mongo(item)
  
    
    
  