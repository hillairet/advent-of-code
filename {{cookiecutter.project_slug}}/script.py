from typer import echo, run


def main():
    with open('data.txt') as challenge_input:
        while line := challenge_input.readline():
            data = line.strip()
            echo(data)

    echo('Print out results here')


if __name__ == '__main__':
    run(main)
