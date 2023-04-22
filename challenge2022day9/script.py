from dataclasses import dataclass
from typing import Set, Tuple

from typer import echo, run


@dataclass
class Knot:
    row: int
    col: int

    def move(self, direction: str) -> None:
        if direction == 'U':
            self.row += 1
        elif direction == 'D':
            self.row -= 1
        elif direction == 'R':
            self.col += 1
        elif direction == 'L':
            self.col -= 1
        else:
            raise ValueError(f'{direction=} is unknown')

    @property
    def tuple(self) -> Tuple[int, int]:
        return (self.row, self.col)

    def __sub__(self, other) -> 'Knot':
        return Knot(row=self.row - other.row, col=self.col - other.col)


def follow_the_lead(lead: Knot, follower: Knot) -> None:
    relative_distance = lead - follower

    if abs(relative_distance.row) < 2 and abs(relative_distance.col) < 2:
        return
    else:
        if abs(relative_distance.row) > 1:
            follower.row = lead.row - int(relative_distance.row / abs(relative_distance.row))
        else:
            follower.row = lead.row
        if abs(relative_distance.col) > 1:
            follower.col = lead.col - int(relative_distance.col / abs(relative_distance.col))
        else:
            follower.col = lead.col


def display_rope(screen: list[int], rope: list[Knot], move: str) -> None:
    print('------------ Head move =>', move)
    display_rope = [knot.tuple for knot in rope]
    display = []
    for r, row in enumerate(range(screen[0], screen[1])):
        display.append([])
        for c, col in enumerate(range(screen[2], screen[3])):
            match_indices = [
                idx for idx in range(len(display_rope)) if display_rope[idx] == (row, col)
            ]
            if not match_indices:
                point = '.'
                if (row, col) == (0, 0):
                    point = 's'
                display[r].append(point)
                continue
            point = str(match_indices[0])
            if point == '0':
                point = 'H'
            if point == str(len(rope) - 1):
                point = 'T'
            display[r].append(point)
    display.reverse()
    for row in display:
        print(''.join(row))


def move_rope(rope: list[Knot], move: str) -> Set[Tuple[int, int]]:
    direction = move.split(' ')[0]
    distance = int(move.split(' ')[1])
    tail_positions = set()

    for step in range(distance):
        rope[0].move(direction=direction)
        for idx in range(len(rope) - 1):
            lead = rope[idx]
            follower = rope[idx + 1]
            follow_the_lead(lead=lead, follower=follower)
            # print('LEAD =>', lead.tuple, '    FOLLOWER =>', follower.tuple)
            if idx == len(rope) - 2:
                tail_positions.add(follower.tuple)

    return tail_positions


def process(data, rope_length: int, printout_move: bool = False) -> int:
    rope = []
    for n_knot in range(rope_length):
        rope.append(Knot(0, 0))

    visited_positions: Set[Tuple[int, int]] = set([rope[-1].tuple])
    for line in data.split('\n'):
        move = line.strip()
        if not move:
            continue
        tail_positions = move_rope(rope=rope, move=move)
        if printout_move:
            display_rope(screen=[-6, 14, -11, 15], rope=rope, move=move)

        visited_positions |= tail_positions

    return len(visited_positions)


def main():
    with open('data.txt') as challenge_input:
        data = challenge_input.read()
        n_visited_positions_2 = process(data, rope_length=2)
        n_visited_positions_10 = process(data, rope_length=10)

    echo(f'Rope length 2, Number of positions visited at least once: {n_visited_positions_2}')
    echo(f'Rope length 10, Number of positions visited at least once: {n_visited_positions_10}')


if __name__ == '__main__':
    run(main)
