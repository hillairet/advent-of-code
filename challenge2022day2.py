from typer import echo, run

convert_to_shape = dict(A='Rock', B='Paper', C='Scissors', X='Rock', Y='Paper', Z='Scissors')
convert_to_score = dict(X=1, Y=2, Z=3, Rock=1, Paper=2, Scissors=3)
convert_to_result = dict(X='loose', Y='draw', Z='win')
me_winning = [('Rock', 'Paper'), ('Paper', 'Scissors'), ('Scissors', 'Rock')]
rules = ['Rock', 'Paper', 'Scissors', 'Rock', 'Paper', 'Scissors']


def part1_score(opponent_shape: str, my_letter: str) -> int:
    my_shape = convert_to_shape[my_letter]
    the_round = (opponent_shape, my_shape)

    score = convert_to_score[my_letter]

    if opponent_shape == my_shape:
        score += 3
    elif the_round in me_winning:
        score += 6

    return score


def part2_score(opponent_shape: str, my_letter: str) -> int:
    my_result = convert_to_result[my_letter]

    if my_result == 'win':
        my_shape = rules[rules.index(opponent_shape) + 1]
        score = convert_to_score[my_shape] + 6
    elif my_result == 'draw':
        my_shape = opponent_shape
        score = convert_to_score[my_shape] + 3
    else:
        my_shape = rules[rules.index(opponent_shape) - 1]
        score = convert_to_score[my_shape]

    return score


def main():
    total_score_part1 = 0
    total_score_part2 = 0
    with open('data/challenge2022day2.txt') as challenge_input:
        while line := challenge_input.readline():
            opponent_letter, my_letter = line.strip().split(' ')
            opponent_shape = convert_to_shape[opponent_letter]

            total_score_part1 += part1_score(opponent_shape, my_letter)
            total_score_part2 += part2_score(opponent_shape, my_letter)

    echo(f'\rThe total score for part 1 is {total_score_part1}')
    echo(f'\rThe total score for part 2 is {total_score_part2}')


if __name__ == '__main__':
    run(main)
