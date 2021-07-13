import pytest
import json as j
import requests as r

test_user = ''


@pytest.mark.run(order=1)
def test_get_user_list():
    res = r.get('http://127.0.0.1:5000/')
    assert res.status_code is 200
    res_data = res.json()
    assert res_data is not None
    assert res_data['users'][0]['id'] == 'f6fe4007'
    assert res_data['users'][0]['name'] == 'Pete Jones'
    assert res_data['users'][0]['location'] == 'London'


@pytest.mark.run(order=2)
def test_post_user_create():
    post_user = {
        'name': 'Rob O Rea',
        'location': 'Dublin'
    }

    res = r.post('http://127.0.0.1:5000/api/user/create',
                 data=j.dumps(post_user))
    global test_user
    test_user = res.json()['id']
    assert res.status_code is 200


@pytest.mark.run(order=3)
def test_get_user():
    res = r.get(f'http://127.0.0.1:5000/api/user/{test_user}')
    assert res.status_code is 200
    res_data = res.json()
    assert res_data is not None
    assert res_data['id'] == test_user


@pytest.mark.run(order=4)
def test_put_user():
    put_user = {
        'name': 'Rea O Rob',
        'location': 'Belfast'
    }

    res = r.put(
        f'http://127.0.0.1:5000/api/user/{test_user}', data=j.dumps(put_user))
    assert res.status_code is 201

    res = r.get(f'http://127.0.0.1:5000/api/user/{test_user}')
    res_data = res.json()
    assert res_data is not None
    assert res_data['name'] == put_user['name']
    assert res_data['location'] == put_user['location']


@pytest.mark.run(order=5)
def test_delete_user():
    res = r.delete(f'http://127.0.0.1:5000/api/user/{test_user}')
    assert res.status_code is 204
