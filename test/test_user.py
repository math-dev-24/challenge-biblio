from Model.user import User
from tinydb import TinyDB
from tinydb.storages import MemoryStorage
import pytest


@pytest.fixture
def setup():
    User.instance = TinyDB(storage=MemoryStorage)


@pytest.fixture
def user(setup):
    user = User(first_name="John", last_name="Doe", password="1234", email="john.doe@gmail.com")
    user.save()
    return user


@pytest.fixture
def get_user(user):
    return user.get_user_by_email(user.email)


def test_user_properties(user):
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.password == "1234"
    assert user.email == "john.doe@gmail.com"


def test_get_user_by_id(get_user, user):
    user_get = user.get_user_by_id(get_user[0]['id'])
    assert user_get[0]['first_name'] == "John"
