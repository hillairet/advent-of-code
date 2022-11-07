from re import search
from typing import Tuple

from numpy import (
    arange,
    array,
    count_nonzero,
    int8,
    logical_and,
    logical_not,
    logical_or,
    logical_xor,
    shape,
    tile,
    zeros,
)
from scipy.sparse import bsr_array
from typer import echo, run


def make_matrix(
    start_row: int, end_row: int, start_col: int, end_col: int, mat_shape: Tuple[int, int]
):
    """Use SciPy's sparse matrix to build the toggle and turn on/off matrices."""
    nb_rows = end_row - start_row + 1
    nb_cols = end_col - start_col + 1

    row = array(arange(start_row, end_row + 1)).repeat(nb_cols)
    col = tile(arange(start_col, end_col + 1), nb_rows)

    data = array(1).repeat(nb_rows * nb_cols)
    matrix = bsr_array((data, (row, col)), shape=mat_shape).toarray()
    return matrix


def toggle(matrix, change_matrix):
    return logical_xor(matrix, change_matrix)


def turn_on(matrix, change_matrix):
    return logical_or(matrix, change_matrix)


def turn_off(matrix, change_matrix):
    return logical_and(matrix, logical_not(change_matrix))


def main():
    lights = zeros((1000, 1000), dtype=int8)

    with open('data/challenge2015day6.txt') as challenge_input:
        while line := challenge_input.readline():
            parsed_line = search(r'([\w\s]+) ([\d]+),([\d]+) through ([\d]+),([\d]+)', line)
            command = parsed_line.group(1)
            start_row = int(parsed_line.group(2))
            end_row = int(parsed_line.group(4))
            start_col = int(parsed_line.group(3))
            end_col = int(parsed_line.group(5))

            change_matrix = make_matrix(
                start_row=start_row,
                end_row=end_row,
                start_col=start_col,
                end_col=end_col,
                mat_shape=shape(lights),
            )
            match command:
                case 'toggle':
                    lights = toggle(matrix=lights, change_matrix=change_matrix)
                case 'turn on':
                    lights = turn_on(matrix=lights, change_matrix=change_matrix)
                case 'turn off':
                    lights = turn_off(matrix=lights, change_matrix=change_matrix)
                case _:
                    raise ValueError(f'Command {command} is unknown')
            echo(f'\rCalculating: {count_nonzero(lights)}', nl=False)

    echo(f'\rThe number of lights on is {count_nonzero(lights)}')


if __name__ == '__main__':
    run(main)
