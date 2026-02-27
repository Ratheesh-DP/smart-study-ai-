# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from database import Session, Student
from model import predict_score

app = FastAPI()

class StudyInput(BaseModel):
    name: str
    subject: str
    study_hours: float

@app.post("/predict/")
def predict(data: StudyInput):
    session = Session()
    
    score = predict_score(data.study_hours)
    
    new_student = Student(
        name=data.name,
        subject=data.subject,
        study_hours=data.study_hours,
        predicted_score=score
    )
    
    session.add(new_student)
    session.commit()
    
    return {
        "message": "Prediction successful",
        "predicted_score": score
    }

@app.get("/students/")
def get_students():
    session = Session()
    students = session.query(Student).all()
    
    return students
