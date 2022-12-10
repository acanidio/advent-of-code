import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [[[int(i) for i in pair.split('-')] for pair in line.split(',')] for line in puzzle_input.split()]


def fully_contains(x, y):
    """Check if x section assignment fully contains y section assignment"""
    return y[0] >= x[0] and y[1] <= x[1]


def part1(data):
    """Solve part 1"""
    return sum([fully_contains(x, y) or fully_contains(y, x) for x, y in data])


def overlap(x, y):
    """Check if x and y section assignments overlap of at least one section"""
    return any([i in range(y[0], y[1] + 1) for i in range(x[0], x[1] + 1)])


def part2(data):
    """Solve part 2"""
    return sum([overlap(x, y) for x, y in data])


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
