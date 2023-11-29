import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from src.shared.domain.repositories.discipline_repository_interface import IDisciplineRepository
from src.shared.infra.dto.DisciplineMongoDTO import DisciplineMongoDTO


load_dotenv()
env = os.environ

class DisciplineRepositoryMongo(IDisciplineRepository):
    def __init__(self):
        self.mongo = MongoClient(env['MONGODB-URI'], server_api=ServerApi('1'))
        self.db = self.mongo[env['MONGODB-NAME']]
        self.collection = self.db[env['MONGODB-DISCIPLINE-COLLECTION']]
        
    def create_discipline(self, new_discipline):
        item = DisciplineMongoDTO.from_entity(new_discipline).to_mongo()
        resp = self.collection.insert_one(item)
        
        return new_discipline
    
    def get_discipline_by_id(self, discipline_id):
        item = self.collection.find_one({"discipline_id": discipline_id})
        resp = None
        if item is not None:
            resp = DisciplineMongoDTO.from_mongo(item).to_entity()
        return resp
    
    def update_discipline_by_id(self, discipline_id, new_name=None, new_year=None, new_students_list=None):
        updated_dict = {}
        if new_name is not None:
            updated_dict['name'] = new_name
        if new_year is not None:
            updated_dict['year'] = new_year
        if new_students_list is not None:
            updated_dict['students_emails_list'] = new_students_list
            
        item = self.collection.find_one_and_update({"discipline_id": discipline_id}, {"$set": updated_dict}, return_document=True)
        
        return DisciplineMongoDTO.from_mongo(item).to_entity()
    
    def delete_discipline(self, discipline_id):
        item = self.collection.find_one({"discipline_id": discipline_id})
        self.collection.delete_one({"discipline_id": discipline_id})
        return DisciplineMongoDTO.from_mongo(item).to_entity()
    
    def batch_create_disciplines(self, disciplines):
        items = [DisciplineMongoDTO.from_entity(discipline).to_mongo() for discipline in disciplines]
        resp = self.collection.insert_many(items)
        return disciplines
    
    def get_all_disciplines(self):
        items = self.collection.find()
        resp = None
        if items is not []:
            resp = [DisciplineMongoDTO.from_mongo(item).to_entity() for item in items]
        return resp