from re import search

from typer import echo, run


def parse_header(input_header: list[str]) -> list[list[str]]:
    number_stacks = int((len(input_header[0]) + 1) / 4)
    crate_stacks = [[] for n in range(number_stacks)]

    for line in reversed(input_header):
        for stack in range(number_stacks):
            character = line[1 + stack * 4 : 2 + stack * 4]
            if character == ' ':
                continue
            crate_stacks[stack].append(character)

    return crate_stacks


def move_crates_1by1(crate_stacks: list[list[str]], move: str) -> None:

    parsed_move = search(r'move (\d+) from (\d+) to (\d+)', move)
    n_crates_to_move = int(parsed_move.group(1))
    from_stack = int(parsed_move.group(2)) - 1
    to_stack = int(parsed_move.group(3)) - 1

    for crate in range(n_crates_to_move):
        crate_stacks[to_stack].append(crate_stacks[from_stack].pop())


def move_crates_inbatch(crate_stacks: list[list[str]], move: str) -> None:

    print(move)
    parsed_move = search(r'move (\d+) from (\d+) to (\d+)', move)
    n_crates_to_move = int(parsed_move.group(1))
    from_stack = int(parsed_move.group(2)) - 1
    to_stack = int(parsed_move.group(3)) - 1

    batch = []
    for crate in range(n_crates_to_move):
        batch.append(crate_stacks[from_stack].pop())

    print(move, crate_stacks[from_stack], crate_stacks[to_stack])
    crate_stacks[to_stack] += reversed(batch)


def get_stack_tops(crate_stacks: list[list[str]]) -> str:
    tops = ''
    for stack in crate_stacks:
        tops += stack[-1]
    return tops


def main():
    with open('data.txt') as challenge_input:
        header = []
        header_done = False
        crate_stacks_part1 = []
        crate_stacks_part2 = []
        while line := challenge_input.readline():
            if not header_done:
                if line.find('[') != -1:
                    header.append(line)
                else:
                    header_done = True
                    crate_stacks_part1 = parse_header(header)
                    crate_stacks_part2 = parse_header(header)
                continue

            # skip stack numbering and empty line
            if line.find('move') == -1:
                continue

            data = line.strip()
            move_crates_1by1(crate_stacks_part1, data)
            move_crates_inbatch(crate_stacks_part2, data)

        tops_part1 = get_stack_tops(crate_stacks_part1)
        tops_part2 = get_stack_tops(crate_stacks_part2)
        echo(f'The crates at the top of the stacks for part 1 are {tops_part1}')
        echo(f'The crates at the top of the stacks for part 2 are {tops_part2}')


if __name__ == '__main__':
    run(main)
