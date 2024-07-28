import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    return [[int(c) for c in line] for line in puzzle_input.split()]


def visible(x, y, data):
    """Check if a specific tree is visible"""
    # Edge trees are always visible
    if x == 0 or y == 0 or (y + 1) == len(data) or (x + 1) == len(data[y]):
        return True

    # Check left line
    if all( [data[y][x] > data[y][i] for i in range(0, x)] ):
        return True

    # Check right line
    if all( [data[y][x] > data[y][i] for i in range(x+1, len(data[y]))] ):
        return True

    # Check top line
    if all( [data[y][x] > data[i][x] for i in range(0, y)] ):
        return True

    # Check bottom line
    if all( [data[y][x] > data[i][x] for i in range(y+1, len(data))] ):
        return True

    # Otherwise the tree is not visible
    return False

def part1(data):
    """Solve part 1"""
    map = [[visible(x, y, data) for x in range(len(data[y]))] for y in range(len(data))]
    return sum([sum(row) for row in map])
    count = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            count += 1 if visible(x, y, data) else 0
    return count


def part2(data):
    """Solve part 2"""
    print( data - data[0][0] )


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
