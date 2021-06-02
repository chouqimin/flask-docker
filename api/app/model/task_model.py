from sqlalchemy import Column, text
from sqlalchemy.types import Integer, String, Boolean, TIMESTAMP

from app import db

class Task(db.Model):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)    
    name = Column(String(45), nullable=False)
    status = Column(Boolean, server_default=text("'0'"))
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    @staticmethod
    def get_list():
        tasks = db.session.query(
            Task.id, 
            Task.name, 
            Task.status
            ).all()

        print(tasks)
        data = {
            'result':[{'id':task.id, 'name':task.name, 'status':task.status} for task in tasks]
        }
        print(data)
        return data

    @staticmethod
    def insert_by_name(name):
        task = Task(name=name)
        db.session.add(task)
        db.session.commit()
        return task.id

    @staticmethod
    def get_by_id(task_id):
        task = db.session.query(Task).filter_by(id=task_id).first()
        return task