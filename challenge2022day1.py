from typer import echo, run


def main():
    with open('data/challenge2022day1.txt') as challenge_input:
        calories = []
        calory_counter = 0
        while line := challenge_input.readline():
            value = line.strip()
            if len(value) == 0:
                calories.append(calory_counter)
                calory_counter = 0
            else:
                calory_counter += int(value)

    sorted_calories = sorted(calories, reverse=True)

    top3_total = sorted_calories[0] + sorted_calories[1] + sorted_calories[2]

    echo(f'\rThe elf with the max amount of calories has {sorted_calories[0]}')
    echo(f'The elves with the top3 max amounts of calories have a total of {top3_total}')


if __name__ == '__main__':
    run(main)
