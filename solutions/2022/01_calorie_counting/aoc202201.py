import pathlib
import sys

def split(list, sep):
    """Split a list into sub-lists when separator is encountered"""
    data = []
    elf = []
    for item in list:
        if item is None:
            data.append( elf )
            elf = []
        else:
            elf.append( item )
    data.append( elf )
    return data


def parse(puzzle_input):
    """Parse input"""
    return split( [int(line) if line else None for line in puzzle_input.split('\n')], None )


def part1(data):
    """Solve part 1"""
    return max([sum(elf) for elf in data])


def part2(data):
    """Solve part 2"""
    return sum( sorted([sum(elf) for elf in data], reverse=True)[:3] )


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
