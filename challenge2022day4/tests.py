from pytest import mark, param

from script import is_fully_contained

params_part1 = [
    param('2-4,6-8', False),
    param('2-3,4-5', False),
    param('5-7,7-9', False),
    param('2-8,3-7', True),
    param('6-6,4-6', True),
    param('2-6,4-8', False),
]


@mark.parametrize('data, expected', params_part1)
def test_part1(data, expected):

    assert is_fully_contained(data) == expected


params_part2 = [
    param('2-4,6-8', False),
    param('2-3,4-5', False),
    param('5-7,7-9', True),
    param('2-8,3-7', True),
    param('6-6,4-6', True),
    param('2-6,4-8', True),
]


@mark.parametrize('some_input, expected_thing', params_part2)
def test_part2(some_input, expected_thing):
    assert some_input == expected_thing
