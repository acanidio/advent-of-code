import pathlib
import re
import sys

def replace_spelled(line: str) -> str:
    REPLACEMENTS = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3ree",
        "four": "f4ur",
        "five": "f5ve",
        "six": "s6x",
        "seven": "s7ven",
        "eight": "e8ght",
        "nine": "n9ne"
    }
    for key, value in REPLACEMENTS.items():
        line = line.replace( key, value )
    return line

def merge(digits: list[int]) -> int:
    return 10 * digits[0] + digits[-1] if digits else 0

def extract_digits(line: str) -> list[int]:
    return [int(character) for character in line if character.isnumeric()]

def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split()]


def part1(data):
    """Solve part 1"""
    return sum( [merge(extract_digits(line)) for line in data] )


def part2(data):
    """Solve part 2"""
    return part1( [replace_spelled(line) for line in data] )


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
