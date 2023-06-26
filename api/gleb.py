import json
import os.path
import pathlib
import time
from unittest import TestCase, main

import requests

from main import app

BASE_URL = '/api/v1/projects'


def auth():
    data = {
        'email': 'glib@zpoken.io',
        'password': '12345678',
        'returnSecureToken': True
    }
    response = requests.post(
        url='https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyA_hu8mFWnFC3huZ_hctQiA3Q918PAbnBo',
        data=json.dumps(data))
    time.sleep(3)
    data = {
        'idToken': response.json()['idToken'],
        'fingerprint': '7f16ce8a1738428678922bb80cf1b5b1478da0b3',
        'role': 'node_runner'
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url="https://dev-mn-admin.zpoken.dev/api/v1/auth", data=json.dumps(data), headers=headers)
    print(response)


class ProjectAPITest(TestCase):
    tester = app.test_client()
    bearer_token = auth(tester)

    def test_create_project(self):
        # file = '/Users/alexriaronc/work/mawari/back-mw/tests/test_data/test.txt'
        # file = open(os.path.join(pathlib.Path().absolute(), '..', 'test_data', 'test.txt'), 'rb')
        file = open(os.path.join(pathlib.Path().absolute(), '.tests', 'test_data', 'test.txt'), 'rb')
        data = {
            "data": '{"name": "unittest_creation", "user_id": 167, "description": "creation via unittest", "country": "ukraine", "category": "test"}',
            "request_files": file
        }
        response = self.tester.post(BASE_URL, content_type='multipart/form-data', data=data)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.json['user_id'] == 167)

    def test_get_all(self):
        response = self.tester.get(BASE_URL, headers={'Authorization': f"Bearer {self.bearer_token}"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data)

    def test_get_selected(self):
        response = self.tester.get(BASE_URL + '/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 1)

    def test_edit_project(self):
        data = {"name": "unittest_editing", "category": "edit_unittest", "country": "usa"}
        response = self.tester.put(BASE_URL + '/1', content_type='application/json', data=json.dumps(data))
        self.assertEqual(200, response.status_code)

    def test_approve_project(self):
        # file = open(os.path.join(pathlib.Path().absolute(), '..', 'test_data', 'test.txt'), 'rb')
        file = open(os.path.join(pathlib.Path().absolute(), '.tests', 'test_data', 'test.txt'), 'rb')
        data = {
            "data": '{"name": "unittest_approve", "user_id": 167, "description": "approve via unittest", "country": "ukraine", "category": "test"}',
            "request_files": file
        }
        response = self.tester.post(BASE_URL, content_type='multipart/form-data', data=data)

        time.sleep(2)

        response = self.tester.post(BASE_URL + f"/{response.json['id']}/approve")
        self.assertEqual(200, response.status_code)

    def test_decline_project(self):
        # file = open(os.path.join(pathlib.Path().absolute(), '..', 'test_data', 'test.txt'), 'rb')
        file = open(os.path.join(pathlib.Path().absolute(), '.tests', 'test_data', 'test.txt'), 'rb')
        data = {
            "data": '{"name": "unittest_decline", "user_id": 167, "description": "decline via unittest", "country": "ukraine", "category": "test"}',
            "request_files": file
        }
        response = self.tester.post(BASE_URL, content_type='multipart/form-data', data=data)

        response = self.tester.post(BASE_URL + f"/{response.json['id']}/decline")
        self.assertEqual(200, response.status_code)

    def test_delete_project(self):
        # file = open(os.path.join(pathlib.Path().absolute(), '..', 'test_data', 'test.txt'), 'rb')
        file = open(os.path.join(pathlib.Path().absolute(), '.tests', 'test_data', 'test.txt'), 'rb')
        data = {
            "data": '{"name": "unittest_delition", "user_id": 167, "description": "delition via unittest", "country": "ukraine", "category": "test"}',
            "request_files": file
        }
        response = self.tester.post(BASE_URL, content_type='multipart/form-data', data=data)
        response = self.tester.delete(BASE_URL + f"/{response.json['id']}")
        self.assertEqual(204, response.status_code)

    def test_get_project_files(self):
        response = self.tester.get(BASE_URL + '/1/files')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[0]['id'], 1)
        self.assertEqual(response.json[0]['filename'], '//home/hlib/back/.tests/api/../test_data/test.txt')

    # def test_send_selected_file(self):
    #     bearer_token = auth(self.tester)
    #     response = self.tester.post(BASE_URL + '/51/files/26/download', headers={'Authorization': f"Bearer {self.bearer_token}"})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json[0]['id'], 26)

    def test_get_project_counters(self):
        response = self.tester.get(BASE_URL + '/counters')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['all'])

    def test_add_project_to_db(self):
        response = self.tester.post(BASE_URL + '/1/download', content_type='multipart/form-data',
                                    data=json.dumps({'guid': '4c1e04d3-4bdd-4629-a445-616f0b390fc4'}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['all'])


if __name__ == '__main__':
    main()