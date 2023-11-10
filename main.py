from fastapi import FastAPI
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.modules.create_user.app.create_user_presenter import create_user_presenter
from src.modules.get_ranking.app.get_ranking_presenter import get_ranking_presenter

from src.modules.get_schedule.app.get_schedule_presenter import get_shedule_presenter
from src.modules.update_schedule.app.update_schedule_presenter import update_schedule_presenter

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

@app.put("/create_user")
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