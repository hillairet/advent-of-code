from typer import echo, run

LETTER_TO_PRIORITY = {chr(i + 97): i + 1 for i in range(26)} | {
    chr(i + 65): i + 27 for i in range(26)
}


def find_shared_item(rucksack: str) -> str:
    midlength = int(len(rucksack) / 2)
    container1 = set(rucksack[:midlength])
    container2 = set(rucksack[midlength:])

    return (container1 & container2).pop()


def find_badge(rucksack_group: list[str]) -> str:
    return (set(rucksack_group[0]) & set(rucksack_group[1]) & set(rucksack_group[2])).pop()


def calculate_priority(item: str) -> int:
    return LETTER_TO_PRIORITY[item]


def main():
    total_priority_part1 = 0
    total_priority_part2 = 0
    rucksack_group = []
    with open('challenge2022day3/data.txt') as challenge_input:
        while line := challenge_input.readline():
            rucksack = line.strip()

            shared_item = find_shared_item(rucksack)
            total_priority_part1 += calculate_priority(shared_item)

            rucksack_group.append(rucksack)
            if len(rucksack_group) == 3:
                badge = find_badge(rucksack_group)
                total_priority_part2 += calculate_priority(badge)
                rucksack_group.clear()

    echo(f'Total priority for part1 = {total_priority_part1}')
    echo(f'Total priority for part2 = {total_priority_part2}')


if __name__ == '__main__':
    run(main)
