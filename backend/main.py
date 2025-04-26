from fastapi import *
import uvicorn
from pydantic import BaseModel
from model import Todo
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

Todo.metadata.create_all(engine)

class TodoCreate(BaseModel):
    title: str
    description: str

class TodoUpdate(BaseModel):
    title: str
    description: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/") #get - подключение/получние данных от сервера 
def start_fastapi():
    return {"message": "FastAPI работает"}

@app.post("/abb_do", tags =['События'], summary='Добавить новое событие') #post - отправлчет данные от сервера
def create_todo(todo:TodoCreate, db: Session = Depends(get_db)): #модель TodoCreate - описана выше
    dbtodo = Todo(title = todo.title, description = todo.description)
    db.add(dbtodo)
    db.commit()
    #db.refresh(dbtodo)
    return {"msg":"Событие добавлено"}

@app.get("/get_todos", tags = ['События'], summary="Посмтреть все события")
def view_all_todos(db:Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos

@app.delete("/todo/{todo_id}", tags = ['События'], summary="Удалить событие по номеру")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail='Такого события не найдено')
    db.delete(todo)
    db.commit()
    return {"msg":"Событие было удалено"}

@app.put("/todo/{todo_id}", tags = ['События'], summary="Изменить событие по номеру")
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    dbtodo = db.query(Todo).filter(Todo.id == todo_id).first()
    if dbtodo is None:
        raise HTTPException(status_code=404, detail='Такого события не найдено')
    dbtodo.title = todo.title
    dbtodo.description = todo.description
    db.commit()
    return {"msg":"Событие изменено"}


@app.post("/abb_us", tags =['Пользователь'], summary='Добавить нового пользователя') #post - отправлчет данные от сервера
def create_todo(todo:TodoCreate, db: Session = Depends(get_db)): #модель TodoCreate - описана выше
    dbtodo = Todo(title = todo.title, description = todo.description)
    db.add(dbtodo)
    db.commit()
    #db.refresh(dbtodo)
    return {"msg":"Пользователь добавлен"}

#@app.get("/hello/{name}", 
#         summary = "Сказать привет", #описание
#         tags = ['🤦‍♂️']) #группирует по тегам можно текст либо эмодзи
#def say_hello(name: str):
#    return{"messege":f"Привет,{name}"}

if __name__ == '__main__': #чтобы был автозапуск на севере
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
