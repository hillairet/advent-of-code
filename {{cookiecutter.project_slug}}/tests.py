from pytest import mark, param

# from script import

params_part1 = [
    param(0, 0),
]


@mark.parametrize('some_input, expected_thing', params_part1)
def test_part1(some_input, expected_thing):
    assert some_input == expected_thing


params_part2 = [
    param(0, 0),
]


@mark.parametrize('some_input, expected_thing', params_part2)
def test_part2(some_input, expected_thing):
    assert some_input == expected_thing
