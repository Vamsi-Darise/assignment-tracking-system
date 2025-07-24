from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

users = []
assignments = []
submissions = []

class User(BaseModel):
    username: str
    password: str
    role: str

class Assignment(BaseModel):
    id: int
    title: str
    description: str
    due_date: str
    created_by: str

class Submission(BaseModel):
    assignment_id: int
    student: str
    content: str
    submitted_at: str

def get_user(username):
    for u in users:
        if u.username == username:
            return u
    return None

@app.post("/signup")
def signup(user: User):
    if get_user(user.username):
        raise HTTPException(status_code=400, detail="User exists")
    users.append(user)
    return {"message": "User registered"}

@app.post("/login")
def login(username: str, password: str):
    user = get_user(username)
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid login")
    return {"token": username}

@app.post("/assignments")
def create_assignment(assignment: Assignment, token: str):
    user = get_user(token)
    if not user or user.role != "teacher":
        raise HTTPException(status_code=403, detail="Only teachers allowed")
    assignments.append(assignment)
    return {"message": "Assignment created"}

@app.post("/assignments/{assignment_id}/submit")
def submit_assignment(assignment_id: int, content: str, token: str):
    user = get_user(token)
    if not user or user.role != "student":
        raise HTTPException(status_code=403, detail="Only students allowed")
    submission = Submission(
        assignment_id=assignment_id,
        student=user.username,
        content=content,
        submitted_at=str(datetime.utcnow())
    )
    submissions.append(submission)
    return {"message": "Submission added"}

@app.get("/assignments/{assignment_id}/submissions")
def view_submissions(assignment_id: int, token: str):
    user = get_user(token)
    if not user or user.role != "teacher":
        raise HTTPException(status_code=403, detail="Only teachers allowed")
    return [s for s in submissions if s.assignment_id == assignment_id]

@app.get("/assignments/{assignment_id}/submissions")
def view_submissions(assignment_id: int, token: str):
    user = get_user(token)
    if not user or user.role != 'teacher':
        raise HTTPException(status_code=403, detail="Only teachers allowed")
    result = [s for s in submissions if s.assignment_id == assignment_id]
    return result