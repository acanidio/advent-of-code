import pathlib
import sys

import re
import string

def parse_stack(stack_input):
    """Parse stack input"""
    lines = stack_input.split('\n')
    positions = [m.start() for m in re.finditer(r"(\d+)", lines[-1])]
    stacks = [[] for _ in range(len(positions))]
    for line in reversed(lines[:-1:]):
        print(f"{line}, {len(line)}")
        for i in range(len(positions)):
            if line[positions[i]] in string.ascii_letters:
                stacks[i].append(positions[i])
    return stacks


def parse_moves(moves_input):
    """Parse stack input"""
    return [[int(item) for item in re.fullmatch(r"move (\d+) from (\d+) to (\d+)", move).groups()] for move in moves_input.split('\n')]


def parse(puzzle_input):
    """Parse input"""
    # Split stack state from moves
    stack_input, moves_input = puzzle_input.split('\n\n')
    return {
        "stack": parse_stack(stack_input),
        "moves": parse_moves(moves_input)
    }


def part1(data):
    """Solve part 1"""
    return data


def part2(data):
    """Solve part 2"""


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
