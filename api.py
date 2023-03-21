import json
import requests

from settings import INVALID_EMAIL, INVALID_PASSWORD


class Pets:
    """ API library to site http://34.141.58.52:8080/#/"""

    def __init__(self):
        # self.my_token = None
        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        """ Request to site swagger to get a users token using the specified email and password """
        data = {"email": 'paratest@mail.ru',
                "password": '1234'}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        print(my_token)
        return my_token, status, my_id

    def get_user_id(self) -> json:
        """The function is used to get user's ID as logged-in user"""  # to be reviewed, should be list of users
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        user_id = res.text
        return status, user_id

    def get_list_users(self) -> json:
        """Request to Swagger to get users list """
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        amount = res.json
        return status, amount

    def add_pet(self) -> json:
        """The function is used to add new pet as logged-in user"""
        my_token = Pets().get_token()[0]
        user_id = Pets().get_user_id()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"name": 'Loy', "type": 'dog', "age": 5, "owner_id": user_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def patch_update_pet(self) -> json:
        """Update the data by pet id"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().add_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id, "name": 'Buddy', "type": 'dog', "age": 2}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def post_pets_list(self) -> json:
        """Get pet list"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id}
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        total = res.json
        return status, total

    def delete_pet(self) -> json:
        """The function is used to delete already existing pet as logged-in user"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().add_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status

    def delete_user(self) -> json:
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        user_id = Pets().get_token()[2]
        res = requests.delete(self.base_url + f'users/{user_id}', headers=headers)
        status = res.status_code
        print(res.json())
        return status

    def login_deleted_user(self) -> json:
        data = {"email": INVALID_EMAIL, "password": INVALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        status = res.status_code
        return status


Pets().get_token()
Pets().get_user_id()
Pets().get_list_users()
Pets().add_pet()
Pets().patch_update_pet()
Pets().post_pets_list()
Pets().delete_pet()
Pets().delete_user()
Pets().login_deleted_user()
