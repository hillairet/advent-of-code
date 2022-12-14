from pytest import mark, param
from script import get_stack_tops, move_crates_1by1, move_crates_inbatch, parse_header

CRATE_STACKS_START = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

params_part1 = [
    param(
        ['    [D]    ', '[N] [C]    ', '[Z] [M] [P]'],
        CRATE_STACKS_START,
        ['move 1 from 2 to 1', 'move 3 from 1 to 3', 'move 2 from 2 to 1', 'move 1 from 1 to 2'],
        'CMZ',
    )
]


@mark.parametrize(
    'input_header, expected_crate_start, moves, expected_stack_tops', params_part1
)
def test_part1(input_header, expected_crate_start, moves, expected_stack_tops):
    crate_stacks = parse_header(input_header)
    assert crate_stacks == expected_crate_start

    for move in moves:
        move_crates_1by1(crate_stacks, move)

    tops = get_stack_tops(crate_stacks)
    assert tops == expected_stack_tops


params_part2 = [
    param(
        ['    [D]    ', '[N] [C]    ', '[Z] [M] [P]'],
        CRATE_STACKS_START,
        ['move 1 from 2 to 1', 'move 3 from 1 to 3', 'move 2 from 2 to 1', 'move 1 from 1 to 2'],
        'MCD',
    )
]


@mark.parametrize(
    'input_header, expected_crate_start, moves, expected_stack_tops', params_part2
)
def test_part2(input_header, expected_crate_start, moves, expected_stack_tops):
    crate_stacks = parse_header(input_header)
    assert crate_stacks == expected_crate_start

    for move in moves:
        move_crates_inbatch(crate_stacks, move)

    tops = get_stack_tops(crate_stacks)
    assert tops == expected_stack_tops
