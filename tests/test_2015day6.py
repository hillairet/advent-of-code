import pytest
from numpy import array, int8

from challenge2015day6 import toggle, turn_off, turn_on


@pytest.fixture
def input_data():
    return dict(
        matrix=array([[False, False], [True, True]], dtype=int8),
        change_matrix=array([[True, False], [True, False]], dtype=int8),
    )


def test_toggle(input_data):
    expected_mat = array([[True, False], [False, True]], dtype=int8)

    toggled_mat = toggle(**input_data)

    assert (toggled_mat == expected_mat).all()


def test_turn_on(input_data):
    expected_mat = array([[True, False], [True, True]], dtype=int8)

    turned_on_mat = turn_on(**input_data)

    assert (turned_on_mat == expected_mat).all()


def test_turn_off(input_data):
    expected_mat = array([[False, False], [False, True]], dtype=int8)

    turned_off_mat = turn_off(**input_data)

    assert (turned_off_mat == expected_mat).all()
