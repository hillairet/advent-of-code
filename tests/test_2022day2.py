import pytest

from challenge2022day2 import part2_score

params = [
    dict(opponent_shape='Rock', my_letter='Y', expected_score=4),
    dict(opponent_shape='Paper', my_letter='X', expected_score=1),
    dict(opponent_shape='Scissors', my_letter='Z', expected_score=7),
]


@pytest.fixture(params=params)
def fixture(request):
    yield request.param


def test_part2_score(fixture):
    score = part2_score(opponent_shape=fixture['opponent_shape'], my_letter=fixture['my_letter'])

    assert score == fixture['expected_score']
