from pytest import mark, param
from script import find_marker

params_part1 = [
    param('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
    param('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
    param('nppdvjthqldpwncqszvftbrmjlhg', 6),
    param('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
    param('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11),
]


@mark.parametrize('data_stream, expected_marker', params_part1)
def test_part1(data_stream, expected_marker):
    found_marker = find_marker(data_stream, 4)
    assert found_marker == expected_marker


params_part2 = [
    param('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
    param('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
    param('nppdvjthqldpwncqszvftbrmjlhg', 23),
    param('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
    param('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26),
]


@mark.parametrize('data_stream, expected_marker', params_part2)
def test_part2(data_stream, expected_marker):
    found_marker = find_marker(data_stream, 14)
    assert found_marker == expected_marker
