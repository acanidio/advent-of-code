import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input


def repeated(seq):
    """Check for a repeated sequence"""
    for i in range(len(seq)):
        for j in range(len(seq)):
            if i != j and seq[i] == seq[j]:
                return True
    return False

def part1(data):
    """Solve part 1"""
    for i in range(4,len(data)):
        if not repeated(data[i-4:i]):
            return i
    return None


def part2(data):
    """Solve part 2"""
    for i in range(14,len(data)):
        if not repeated(data[i-14:i]):
            return i
    return None


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
