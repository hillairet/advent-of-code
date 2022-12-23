from dataclasses import dataclass

from typer import echo, run


def convert_to_list_grid(input_grid: str) -> list[list[str]]:
    grid = []
    for row in input_grid.split('\n'):
        if len(row) > 3:
            grid.append([int(value) for value in list(row)])
    return grid


@dataclass
class Visibility:
    top: bool = False
    bottom: bool = False
    left: bool = False
    right: bool = False

    @property
    def is_visible(self):
        return self.top or self.bottom or self.left or self.right


@dataclass
class Scenery:
    top: int = 0
    bottom: int = 0
    left: int = 0
    right: int = 0

    @property
    def score(self):
        return self.top * self.bottom * self.left * self.right


def get_visibility(grid: list[list[str]], row: int, column: int) -> Visibility:
    highest_top_tree = max([grid[row_idx][column] for row_idx in range(row)] or [-1])
    highest_bottom_tree = max(
        [grid[row_idx][column] for row_idx in range(row + 1, len(grid))] or [-1]
    )
    highest_left_tree = max([grid[row][col_idx] for col_idx in range(column)] or [-1])
    highest_right_tree = max(
        [grid[row][col_idx] for col_idx in range(column + 1, len(grid[row]))] or [-1]
    )

    tree_height = grid[row][column]

    return Visibility(
        top=tree_height > highest_top_tree,
        bottom=tree_height > highest_bottom_tree,
        left=tree_height > highest_left_tree,
        right=tree_height > highest_right_tree,
    )


def get_number_visible_trees(grid: list[list[str]]) -> int:
    n_visible_trees = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            visibility = get_visibility(grid=grid, row=row, column=column)
            if visibility.is_visible:
                n_visible_trees += 1

    return n_visible_trees


def count_visible_trees(trees: list[str], start_tree_height: int, reverse: bool = False) -> int:
    count = 0
    tree_list = reversed(trees) if reverse else trees
    for tree in tree_list:
        count += 1
        if tree >= start_tree_height:
            break
    return count


def get_scenery(grid: list[list[str]], row: int, column: int) -> Scenery:
    tree_height = grid[row][column]

    visible_top_trees = count_visible_trees(
        trees=[grid[row_idx][column] for row_idx in range(row)],
        start_tree_height=tree_height,
        reverse=True,
    )
    visible_bottom_trees = count_visible_trees(
        trees=[grid[row_idx][column] for row_idx in range(row + 1, len(grid))],
        start_tree_height=tree_height,
    )
    visible_left_trees = count_visible_trees(
        trees=[grid[row][col_idx] for col_idx in range(column)],
        start_tree_height=tree_height,
        reverse=True,
    )
    visible_right_trees = count_visible_trees(
        trees=[grid[row][col_idx] for col_idx in range(column + 1, len(grid[row]))],
        start_tree_height=tree_height,
    )

    return Scenery(
        top=visible_top_trees,
        bottom=visible_bottom_trees,
        left=visible_left_trees,
        right=visible_right_trees,
    )


def get_highest_scenic_score(grid: list[list[str]]) -> int:
    highest_scenic_score = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            scenery = get_scenery(grid=grid, row=row, column=column)
            highest_scenic_score = max(scenery.score, highest_scenic_score)

    return highest_scenic_score


def main():
    with open('data.txt') as challenge_input:
        input_grid = challenge_input.read()
        grid = convert_to_list_grid(input_grid)

        total_visible = get_number_visible_trees(grid)
        scenic_score = get_highest_scenic_score(grid)

        echo(f'There are {total_visible} visible trees')
        echo(f'The highest_scenic_score is {scenic_score}')


if __name__ == '__main__':
    run(main)
