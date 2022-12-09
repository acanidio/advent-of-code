import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]


def part1(data):
    """Solve part 1"""
    for x in data:
        for y in data:
            if x + y == 2020:
                return x * y


def part2(data):
    """Solve part 2"""
    for x in data:
        for y in data:
            for z in data:
                if x + y + z == 2020:
                    return x * y * z


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
