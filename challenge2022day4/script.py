from typer import echo, run


def str_range_to_list(str_range):
    start = int(str_range.split('-')[0])
    end = int(str_range.split('-')[1]) + 1

    return range(start, end)


def data_to_sections(data):
    range1, range2 = data.split(',')
    section1 = set(str_range_to_list(range1))
    section2 = set(str_range_to_list(range2))
    return section1, section2


def is_fully_contained(data):
    section1, section2 = data_to_sections(data)

    overlap = section1 & section2
    return (overlap == section1 or overlap == section2)


def is_overlapping(data):
    section1, section2 = data_to_sections(data)

    overlap = section1 & section2
    return bool(len(overlap))


def main():
    number_fully_contained = 0
    number_overlapping = 0
    with open('data.txt') as challenge_input:
        while line := challenge_input.readline():
            data = line.strip()

            number_fully_contained += int(is_fully_contained(data))
            number_overlapping += int(is_overlapping(data))

    echo(f'The number of fully contained sections is {number_fully_contained}')
    echo(f'The number of overlapping sections is {number_overlapping}')


if __name__ == '__main__':
    run(main)
