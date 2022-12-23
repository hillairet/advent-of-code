from script import find_dir_size_to_delete, parse_terminal_output

TERMINAL_OUTPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

DIR_SIZES = {'/a/e': 584, '/a': 94853, '/d': 24933642, '/': 48381165}
MIN_SIZE_TO_DELETE = 24933642


def test():
    dir_sizes = parse_terminal_output(TERMINAL_OUTPUT)
    assert dir_sizes == DIR_SIZES

    dir_size_to_delete = find_dir_size_to_delete(dir_sizes)
    assert dir_size_to_delete == MIN_SIZE_TO_DELETE
