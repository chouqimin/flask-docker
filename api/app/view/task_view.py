from flask_restful import Resource, reqparse

from app.model.task_model import Task
from app import db

class TaskCR(Resource):
    
    parser = reqparse.RequestParser()

    def get(self):
        return Task.get_list()

    def post(self):
        parser = self.parser
        
        parser.add_argument(name='name', required=True, help='key "name" is require')
        post_data = parser.parse_args()
        name = post_data['name']

        id = Task.insert_by_name(name)
        return {'result': {'name': name, 'status': 0, 'id': id}}, 201

class TaskUD(Resource):

    parser = reqparse.RequestParser()

    def put(self, task_id):
        parser = self.parser
        parser.add_argument(name='id', type=int, required=True, help="key 'id' is require")
        parser.add_argument(name='name', required=True, help="key 'name' is require")
        parser.add_argument(name='status', type=int, choices=[0, 1], required=True, help="key 'status' is require，0=Incomplete、1=Complete")
        post_data = parser.parse_args()

        form_id = post_data['id']
        if task_id != form_id:
            return {'message':f'your put id is different, url is {task_id}, form data is {form_id}'}
        task = Task.get_by_id(task_id)
        if task is None:
            return {'message':f'id = {task_id} does not exist'}

        # update
        task.status = post_data['status']
        task.name = post_data['name']
        db.session.commit()
        return {'message':'success update'}, 200

    def delete(self, task_id):
        task = Task.get_by_id(task_id)
        if task is None:
            return {'message':f'id = {task_id} does not exist'}
        db.session.delete(task)
        db.session.commit()
        return {'message':'success delete'}, 200