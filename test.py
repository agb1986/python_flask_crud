import requests as r


def test_get_user_list():
    d = r.get('http://127.0.0.1:5000/').json()
    assert d is not None
