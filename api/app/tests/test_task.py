import unittest
import json

from app import create_app, db

class TestTask(unittest.TestCase):

    def setUp(self):
        '''測試環境搭建'''
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.app_context = self.app.app_context()

        with self.app_context:
            db.create_all()

    def tearDown(self):
        '''測試環境的數據清理&刪除'''
        with self.app_context:
            db.session.remove()
            db.drop_all()

    def test_task_create(self):
        self.post()
        self.get()
        self.delete()
        self.put()

    def check(self, res, key, status_code, want_data):
        '''檢查status_code以及回傳資料'''
        self.assertEqual(res.status_code, status_code)
        res_data = json.loads(res.get_data())
        self.assertEqual(res_data.get(key), want_data)

    def post(self):
        want_data = {'id':1, 'name':'買晚餐', 'status':0}
        # post 第一筆
        res = self.client().post('/task', data={"name":"買晚餐"})
        self.check(res, 'result', 201, want_data)

        # post 第二筆
        res = self.client().post('/task', data={"name":"買晚餐"})
        want_data['id'] += 1
        self.check(res, 'result', 201, want_data)

    def get(self):
        want_data = [
            {'id':1, 'name':'買晚餐', 'status':0},
            {'id':2, 'name':'買晚餐', 'status':0}
            ]    
        res = self.client().get('/task')
        self.check(res, 'result', 200, want_data)

    def put(self):
        # 更新2的資料
        want_data = {'id':2, 'name':'你好', 'status':1}
        res = self.client().put('/task/2', data=want_data)
        self.check(res, 'message', 200, 'success update')

        # 檢查2的資料是否有無修改
        res = self.client().get('/task')
        self.check(res, 'result', 200, [want_data])
    
    def delete(self):
        # 刪除1
        res = self.client().delete('task/1')
        self.check(res, 'message', 200, 'success delete')
        # 檢查1是否刪除(只剩2)
        res = self.client().get('/task')
        want_data = [{'id':2, 'name':'買晚餐', 'status':0}]
        self.check(res, 'result', 200, want_data)
