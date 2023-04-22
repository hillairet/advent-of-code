from pytest import mark, param
from script import Knot, follow_the_lead, process

params_move = [param(Knot(2, 2), Knot(0, 0), (1, 1))]
params_move = [param(Knot(2, 1), Knot(0, 0), (1, 1))]
params_move = [param(Knot(1, 2), Knot(0, 0), (1, 1))]
params_move = [param(Knot(1, 1), Knot(0, 0), (0, 0))]


@mark.parametrize('lead, follower, follower_expected_position', params_move)
def test_move(lead, follower, follower_expected_position):
    follow_the_lead(lead=lead, follower=follower)

    assert follower.tuple == follower_expected_position


params_n_pos = [
    param('R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2', 2, 13),
    param('R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2', 10, 1),
    param('R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20', 10, 36),
]


@mark.parametrize('data, rope_length, expected_n_visited_positions', params_n_pos)
def test_n_positions(data, rope_length, expected_n_visited_positions):
    n_visited_positions = process(data, rope_length=rope_length, printout_move=True)

    assert n_visited_positions == expected_n_visited_positions
