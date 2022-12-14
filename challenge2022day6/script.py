from typer import echo, run


def find_marker(data_stream: str, batch_length: int) -> int:
    for batch_index in range(len(data_stream) - batch_length + 1):
        batch_str = data_stream[batch_index : batch_index + batch_length]
        if len(set(batch_str)) < batch_length:
            continue
        return batch_index + batch_length

    return -1


def main():
    with open('data.txt') as challenge_input:
        line = challenge_input.readline()
        data_stream = line.strip()
        found_marker4 = find_marker(data_stream, 4)
        found_marker14 = find_marker(data_stream, 14)

        echo(f'Marker for batch 4 found at position {found_marker4}')
        echo(f'Marker for batch 14 found at position {found_marker14}')


if __name__ == '__main__':
    run(main)
