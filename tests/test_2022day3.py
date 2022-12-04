from pytest import mark, param

from challenge2022day3 import calculate_priority, find_badge, find_shared_item

params_part1 = [
    param('vJrwpWtwJgWrhcsFMMfFFhFp', 'p', 16),
    param('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'L', 38),
    param('PmmdzqPrVvPwwTWBwg', 'P', 42),
    param('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'v', 22),
    param('ttgJtRGJQctTZtZT', 't', 20),
    param('CrZsJsPPZsGzwwsLwLmpwMDw', 's', 19),
]


@mark.parametrize('rucksack, expected_shared_item, expected_priority', params_part1)
def test_rucksack_priority(rucksack, expected_shared_item, expected_priority):
    shared_item = find_shared_item(rucksack)
    assert shared_item == expected_shared_item

    priority = calculate_priority(shared_item)
    assert priority == expected_priority


params_part2 = [
    param(
        ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg'],
        'r',
        18,
    ),
    param(
        ['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw'], 'Z', 52
    ),
]


@mark.parametrize('rucksack_group, expected_badge, expected_priority', params_part2)
def test_group_priority(rucksack_group, expected_badge, expected_priority):
    shared_item = find_badge(rucksack_group)
    assert shared_item == expected_badge

    priority = calculate_priority(shared_item)
    assert priority == expected_priority
