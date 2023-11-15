from fastapi import FastAPI, HTTPException, status, File, UploadFile
import csv
import codecs
from fastapi.responses import JSONResponse
from src.modules.create_user.app.create_user_presenter import create_user_presenter
from src.modules.delete_user.app.delete_user_presenter import delete_user_presenter
from src.modules.get_ranking.app.get_ranking_presenter import get_ranking_presenter

from src.modules.get_schedule.app.get_schedule_presenter import get_shedule_presenter
from src.modules.get_user.app.get_user_presenter import get_user_presenter
from src.modules.update_schedule.app.update_schedule_presenter import update_schedule_presenter
from src.modules.update_user.app.update_user_presenter import update_user_presenter

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
  return JSONResponse(status_code=exc.status_code, content=exc.detail)

@app.get("/get_schedule")
def get_schedule():
  event = {}
  
  response = get_shedule_presenter(event, None)
  
  return response

@app.put("/update_schedule")
def update_schedule(data: dict = None):
  if data is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  
  event = {
    "body": {
        k: str(v) for k, v in data.items()
    }
  }
  
  for key in data.keys():
    if type(data[key]) == dict:
      event["body"][key] = {
        k: str(v) for k, v in data[key].items()
      }
    
  response = update_schedule_presenter(event, None)
  
  return response

@app.get("/get_ranking")
def get_ranking():
  event = {}
  
  response = get_ranking_presenter(event, None)
  
  return response

@app.put("/create_user", status_code=status.HTTP_201_CREATED)
def create_user(data: dict = None):
  if data is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  
  event = {
    "body": {
        k: str(v) for k, v in data.items()
    }
  }
  
  for key in data.keys():
    if type(data[key]) == dict:
      event["body"][key] = {
        k: str(v) for k, v in data[key].items()
      }
    
  response = create_user_presenter(event, None)
  
  return response

@app.get("/get_user")
def get_user(email: str = None):
  request = {
    "body": {},
    "headers": {},
    "query_params" : {"email": email}
  }
  
  response = get_user_presenter(request, None)
  
  return response

@app.patch("/update_user")
def update_user(data: dict = None):
  if data is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  
  event = {
    "body": {
        k: str(v) for k, v in data.items()
    }
  }
  
  for key in data.keys():
    if type(data[key]) == dict:
      event["body"][key] = {
        k: str(v) for k, v in data[key].items()
      }
    
  response = update_user_presenter(event, None)
  
  return response

@app.delete("/delete_user")
def delete_user(email: str = None):
  if email is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  
  request = {
    "body": {},
    "headers": {},
    "query_params" : {"email": email}
  }
  
  response = delete_user_presenter(request, None)
  
  return response


@app.post("/batch_create_users", status_code=status.HTTP_201_CREATED)
def batch_create_users(file: UploadFile = File(...)):
  csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
  return list(csvReader)