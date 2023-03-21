from api import Pets


pt = Pets()


def test_get_token():
    status = pt.get_token()[1]
    token = pt.get_token()[0]
    assert token
    assert status == 200


def test_get_user_id():
    status = pt.get_user_id()[0]
    user_id = pt.get_user_id()[1]
    assert status == 200
    assert user_id


def test_list_users():
    status = pt.get_list_users()[0]
    amount = pt.get_list_users()[1]
    assert status == 200
    assert amount


def test_add_pet():
    pet_id = pt.add_pet()[0]
    status_add_pet = pt.add_pet()[1]
    assert pet_id
    assert status_add_pet == 200


def test_post_pets_list():
    status = pt.get_token()[1]
    total = pt.post_pets_list()
    assert status == 200
    assert total


def test_update_pet():
    status = pt.patch_update_pet()
    assert status == 200


def test_delete_pet():
    status = pt.delete_pet()
    assert status == 200


def test_delete_user():
    status = pt.delete_user()
    assert status == 200


def test_login_as_deleted_user():
    status = pt.login_deleted_user()
    assert status == 400
