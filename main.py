from fastapi import FastAPI, HTTPException, status, File, UploadFile
import csv
import codecs
from fastapi.responses import JSONResponse
from src.modules.batch_create_disciplines.app.batch_create_disciplines_presenter import batch_create_disciplines_presenter
from src.modules.create_discipline.app.create_discipline_presenter import create_discipline_presenter
from src.modules.create_exercise.app.create_exercise_presenter import create_exercise_presenter
from src.modules.batch_create_users.app.batch_create_users_presenter import batch_create_users_presenter
from src.modules.create_user.app.create_user_presenter import create_user_presenter
from src.modules.delete_discipline.app.delete_discipline_presenter import delete_discipline_presenter
from src.modules.create_answer.app.create_answer_presenter import create_answer_presenter
from src.modules.create_exercise.app.create_exercise_presenter import create_exercise_presenter
from src.modules.batch_create_users.app.batch_create_users_presenter import batch_create_users_presenter
from src.modules.create_user.app.create_user_presenter import create_user_presenter
from src.modules.delete_answer.app.delete_answer_presenter import delete_answer_presenter
from src.modules.delete_exercise.app.delete_exercise_presenter import delete_exercise_presenter
from src.modules.delete_user.app.delete_user_presenter import delete_user_presenter
from src.modules.get_all_disciplines.app.get_all_disciplines_presenter import get_all_disciplines_presenter
from src.modules.get_all_exercises.app.get_all_exercises_presenter import get_all_exercises_presenter
from src.modules.get_discipline.app.get_discipline_presenter import get_discipline_presenter
from src.modules.get_answer.app.get_answer_presenter import get_answer_presenter
from src.modules.get_answers.app.get_answers_presenter import get_answers_presenter
from src.modules.get_exercise.app.get_exercise_presenter import get_exercise_presenter
from src.modules.get_ranking.app.get_ranking_presenter import get_ranking_presenter
from src.modules.get_schedule.app.get_schedule_presenter import get_shedule_presenter
from src.modules.get_user.app.get_user_presenter import get_user_presenter
from src.modules.update_discipline.app.update_discipline_presenter import update_discipline_presenter
from src.modules.update_answer.app.update_answer_presenter import update_answer_presenter
from src.modules.update_exercise.app.update_exercise_presenter import update_exercise_presenter
from src.modules.update_schedule.app.update_schedule_presenter import update_schedule_presenter
from src.modules.update_user.app.update_user_presenter import update_user_presenter
from fastapi.middleware.cors import CORSMiddleware

from src.modules.validate_answer.app.validate_answer_presenter import validate_answer_presenter
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
  return JSONResponse(status_code=exc.status_code, content=exc.detail)

@app.exception_handler(Exception)
async def exception_handler(request, exc):
  return JSONResponse(status_code=500, content=str(exc))


@app.get("/")
def read_root():
  return {"message" : "Monitoria API is running!"}

# Schedule

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

# User

@app.get("/get_ranking")
def get_ranking():
  event = {}
  
  response = get_ranking_presenter(event, None)
  
  return response

@app.post("/create_user", status_code=status.HTTP_201_CREATED)
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
        k: v for k, v in data.items()
    }
  }
  
  for key in data.keys():
    if type(data[key]) == dict:
      event["body"][key] = {
        k: v for k, v in data[key].items()
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

# Exercise

@app.get("/get_all_exercises")
def get_all_exercises():
  event = {}
  
  response = get_all_exercises_presenter(event, None)
  
  return response

@app.post("/create_exercise", status_code=status.HTTP_201_CREATED)
def create_exercise(data: dict = None):
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
    
  response = create_exercise_presenter(event, None)
  
  return response

@app.get("/get_exercise")
def get_exercise(exercise_id: str = None):
  if exercise_id is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  
  request = {
    "body": {},
    "headers": {},
    "query_params" : {"exercise_id": exercise_id}
  }
  
  response = get_exercise_presenter(request, None)
  
  return response

@app.delete("/delete_exercise")
def delete_exercise(exercise_id: str = None):
  if exercise_id is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  
  request = {
    "body": {},
    "headers": {},
    "query_params" : {"exercise_id": exercise_id}
  }
  
  response = delete_exercise_presenter(request, None)
  
  return response

@app.patch("/update_exercise")
def update_exercise(data: dict = None):
  if data is None:
    raise HTTPException(status_code=400, detail="Invalid request body")

  event = {
    "body": {
        k: v for k, v in data.items()
    }
  }
  response = update_exercise_presenter(event, None)
  
  return response

@app.post("/batch_create_users", status_code=status.HTTP_201_CREATED)
def batch_create_users(file: UploadFile = File(...)):
  if file is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  elif file.filename.split(".")[-1] != "csv":
    raise HTTPException(status_code=400, detail="File should be csv format")
  csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
  event = {
    "body": {
      "users": []
    }
  }
  for row in csvReader:
    event["body"]["users"].append(row)
    
  response = batch_create_users_presenter(event, None)

  return response

# Discipline

@app.post("/batch_create_disciplines", status_code=status.HTTP_201_CREATED)
def batch_create_disciplines(file: UploadFile = File(...)):
  if file is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  elif file.filename.split(".")[-1] != "csv":
    raise HTTPException(status_code=400, detail="File should be csv format")
  csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
  event = {
    "body": {
      "disciplines": []
    }
  }
  for row in csvReader:
    event["body"]["disciplines"].append(row)
    
  response = batch_create_disciplines_presenter(event, None)

  return response

@app.get("/get_all_disciplines")
def get_all_disciplines():
  event = {}
  
  response = get_all_disciplines_presenter(event, None)
  
  return response

@app.get("/get_discipline")
def get_discipline(discipline_id: str = None):
  if discipline_id is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  
  request = {
    "body": {},
    "headers": {},
    "query_params" : {"discipline_id": discipline_id}
  }
  
  response = get_discipline_presenter(request, None)
  
  return response

@app.delete("/delete_discipline")
def delete_discipline(discipline_id: str = None):
  if discipline_id is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  
  request = {
    "body": {},
    "headers": {},
    "query_params" : {"discipline_id": discipline_id}
  }
  
  response = delete_discipline_presenter(request, None)
  
  return response

@app.post("/create_discipline", status_code=status.HTTP_201_CREATED)
def create_discipline(data: dict = None):
  if data is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
    
@app.get("/get_answers", status_code=status.HTTP_200_OK)
def get_answers(exercise_id: str = None):
  if exercise_id is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  
  request = {
    "body": {},
    "headers": {},
    "query_params" : {"exercise_id": exercise_id}
  }
  
  response = get_answers_presenter(request, None)
  
  return response

@app.patch("/update_discipline")
def update_discipline(data: dict = None):
  if data is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  
  event = {
    "body": {
        k: v for k, v in data.items()
    }
  }
  
  for key in data.keys():
    if type(data[key]) == dict:
      event["body"][key] = {
        k: str(v) for k, v in data[key].items()
      }
  
  response = update_answer_presenter(event, None)
  
  return response

# Answer


@app.post("/create_answer", status_code=status.HTTP_201_CREATED)
def create_answer(data: dict = None):
  if data is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  
  event = {
    "body": {
        k: v for k, v in data.items()
    }
  }
  
  for key in data.keys():
    if type(data[key]) == dict:
      event["body"][key] = {
        k: str(v) for k, v in data[key].items()
      }
  
  response = create_answer_presenter(event, None)
  
  return response

@app.delete("/delete_answer", status_code=status.HTTP_200_OK)
def delete_answer(data: dict = None):
  if data is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  
  event = {
    "body": {
        k: v for k, v in data.items()
    }
  }
  
  response = delete_answer_presenter(event, None)
  
  return response

@app.patch("/update_answer", status_code=status.HTTP_200_OK)
def update_answer(data: dict = None):
  if data is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  event = {
    "body": {
        k: v for k, v in data.items()
    }
  }
  
  response = create_discipline_presenter(event, None)
  
  return response

@app.get("/get_answer", status_code=status.HTTP_200_OK)
def get_answer(answer_id: str = None):
  if answer_id is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  
  request = {
    "body": {},
    "headers": {},
    "query_params" : {"answer_id": answer_id}
  }
  
  response = get_answer_presenter(request, None)
  
  return response

@app.post("/validate_answer", status_code=status.HTTP_200_OK)
def validate_answer(data: dict = None):
  if data is None:
    raise HTTPException(status_code=400, detail="Invalid request body")
  
  event = {
    "body": {
        k: v for k, v in data.items()
    }
  }
  
  response = validate_answer_presenter(event, None)
  
  return response