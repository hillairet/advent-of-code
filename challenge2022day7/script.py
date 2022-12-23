from collections import defaultdict

from typer import echo, run


def count_file_size(current_path: list[str], dir_sizes: dict[str, int], ls_line: str) -> None:
    if ls_line.startswith('dir'):
        return

    file_size = int(ls_line.split(' ')[0])

    current_full_path = ''
    for depth in range(len(current_path)):
        current_full_path = '/' + '/'.join(current_path[1 : depth + 1])

        dir_sizes[current_full_path] += file_size


def interpret_command(line: str, start_path: list[str]) -> list[str]:
    command = line[2:4]

    if command == 'ls':
        return start_path

    if command != 'cd':
        raise ValueError(f'UNKNOWN command {command}')

    argument = line[5:]
    if argument == '/':
        return ['/']
    elif argument == '..':
        return start_path[:-1]
    else:
        return start_path + [argument]


def parse_terminal_output(terminal_output: str) -> dict[str, int]:
    dir_sizes = defaultdict(lambda: 0)
    current_path = []
    for line in terminal_output.split('\n'):
        if line.startswith('$'):
            current_path = interpret_command(line=line, start_path=current_path)
        elif line == '':
            continue
        else:
            count_file_size(current_path=current_path, dir_sizes=dir_sizes, ls_line=line)

    return dir_sizes


def calculate_total_lt_100k(dir_sizes: dict[str, int]) -> int:
    total_lt_100k = 0
    for size in dir_sizes.values():
        if size > 100000:
            continue
        total_lt_100k += size


def find_dir_size_to_delete(dir_sizes: dict[str, int]) -> int:
    unused_space = 70000000 - dir_sizes['/']
    space_needed = 30000000 - unused_space
    min_size_to_delete = 70000000

    for size in dir_sizes.values():
        print(size, space_needed)
        if size >= space_needed:
            min_size_to_delete = min(min_size_to_delete, size)
            print(min_size_to_delete)

    return min_size_to_delete


def main():
    with open('data.txt') as challenge_input:
        terminal_output = challenge_input.read()
        dir_sizes = parse_terminal_output(terminal_output)

        total_lt_100k = calculate_total_lt_100k(dir_sizes)
        dir_size_to_delete = find_dir_size_to_delete(dir_sizes)

        echo(f'Total size of directories below 100000 is {total_lt_100k}')
        echo(f'The size of the smallest directory to delete is {dir_size_to_delete}')


if __name__ == '__main__':
    run(main)
