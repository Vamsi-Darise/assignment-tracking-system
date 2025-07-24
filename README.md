Assignment Tracking System - Part A: System Design
 1. System Architecture
 Frontend (React/HTML)
        |
     HTTP
        |
 FastAPI Backend Application
        |
     ORM (Pydantic/SQLAlchemy)
        |
 Database (SQLite/PostgreSQL)
 2. Core Entities and Relationships- User: username, password, role (student or teacher)- Assignment: id, title, description, due_date, created_by- Submission: assignment_id, student, content, submitted_at
 Relationships:- One teacher can create many assignments.- One student can submit many assignments.- One assignment can have many submissions.
 3. API Endpoints
 POST   /signup                         - Register new user
 POST   /login                          - Login and return token
 POST   /assignments                    - Create assignment (Teacher)
 POST   /assignments/{id}/submit        - Submit assignment (Student)
GET    /assignments/{id}/submissions   - View submissions (Teacher)
 4. Authentication Strategy- Token-based auth using username as token (simple model).- Backend checks user existence and role.- Role-based access:
  Teacher: Create/view submissions
  Student: Submit assignments
 5. Future Scalability- Use JWT for secure authentication.- Move from SQLite to PostgreSQL/MySQL.- Enable file uploads.- Add teacher/student dashboards.- Deploy using Docker + AWS/GCP.- Add monitoring/logging tools.- Use Redis/Celery for async task queues
