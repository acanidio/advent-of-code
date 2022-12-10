import pathlib
import sys
import string

def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split()]


def split_bag(bag):
    """Split a bag into their compartments"""
    return [bag[:len(bag)//2], bag[len(bag)//2:], None]

def find_common(x, y, z=None):
    """Find element available in both lists"""
    for i in x:
        if i in y:
            if z is None or i in z:
                return i
    return None

def to_priority(c):
    """Convert character to priority"""
    return string.ascii_letters.find(c) + 1


def part1(data):
    """Solve part 1"""
    return sum([to_priority(find_common(*split_bag(bag))) for bag in data])


def part2(data):
    """Solve part 2"""
    badges = []
    for i in range(len(data)//3):
        badges.append(to_priority(find_common(*data[3*i:3*(i+1)])))
    return sum(badges)


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
