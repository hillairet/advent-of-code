from pytest import mark, param
from script import (
    Scenery,
    Visibility,
    convert_to_list_grid,
    get_highest_scenic_score,
    get_number_visible_trees,
    get_scenery,
    get_visibility,
)

INPUT_GRID = """30373
25512
65332
33549
35390"""

GRID = convert_to_list_grid(INPUT_GRID)

params_part1 = [
    param(1, 1, Visibility(top=True, left=True)),
    param(1, 2, Visibility(top=True, left=False, right=True)),
    param(1, 3, Visibility()),
    param(2, 1, Visibility(right=True)),
    param(2, 2, Visibility()),
    param(2, 3, Visibility(right=True)),
    param(3, 1, Visibility()),
    param(3, 2, Visibility(bottom=True, left=True)),
    param(3, 3, Visibility()),
    param(0, 0, Visibility(top=True, left=True)),
    param(4, 4, Visibility(bottom=True, right=True)),
]


@mark.parametrize('row, column, expected_visibility', params_part1)
def test_part1_one_tree(row, column, expected_visibility):
    visibility = get_visibility(grid=GRID, row=row, column=column)

    assert visibility == expected_visibility


def test_part1_forest():
    total_visible = get_number_visible_trees(GRID)

    assert total_visible == 21


params_part2 = [
    param(1, 2, Scenery(top=1, bottom=2, left=1, right=2), 4),
    param(3, 2, Scenery(top=2, bottom=1, left=2, right=2), 8),
]


@mark.parametrize('row, column, expected_scenery, expected_score', params_part2)
def test_part2_scenery(row, column, expected_scenery, expected_score):

    scenery = get_scenery(grid=GRID, row=row, column=column)

    assert scenery == expected_scenery
    assert scenery.score == expected_score


def test_part2_highest_scenic_score():
    scenic_score = get_highest_scenic_score(GRID)

    assert scenic_score == 8
