import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [ [int(x) for x in line.split('   ')] for line in puzzle_input.split('\n') ]


def part1(data):
    """Solve part 1"""
    first  = sorted( [x[0] for x in data] )
    second = sorted( [x[1] for x in data] )
    return sum([ abs(x[0] - x[1]) for x in zip(first, second) ])


def part2(data):
    """Solve part 2"""
    first  = [x[0] for x in data]
    second = sorted( [x[1] for x in data] )
    return sum( [x * second.count(x) for x in first] )


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
