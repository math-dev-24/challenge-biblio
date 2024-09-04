from Model.movement import MovementBook
from tinydb import TinyDB
from tinydb.storages import MemoryStorage
import pytest
import datetime


@pytest.fixture
def setup():
    MovementBook.instance = TinyDB(storage=MemoryStorage)


@pytest.fixture
def movement(setup):
    user_id = 76
    start_date = datetime.datetime.now()
    end_date = start_date + datetime.timedelta(days=1)
    movement = MovementBook(isbn="1234443", user_id=user_id, date_start=start_date, date_end=end_date)
    movement.register()
    return movement


def test_delete_movement_by_isbn(movement):
    is_delete: bool = movement.delete_movement_by_isbn(movement._isbn)
    assert is_delete is True


def test_delete_movement_by_user_id(movement):
    is_delete: bool = movement.delete_movement_by_user_id(movement.user_id)
    assert is_delete is True


def test_movement_today(movement):
    today = datetime.datetime.now()
    movements = movement.get_all_movements_in_today(today)
    assert len(movements) > 0
