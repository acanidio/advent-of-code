import math
import pathlib
import re
import sys

def parse_set(set: str) -> dict:
    base = { color: int(n) for n, color in re.findall( r'(\d+) (red|green|blue)', set ) }
    return { color: base[color] if color in base.keys() else 0 for color in ['red', 'green', 'blue'] }

def parse_game(game: str) -> dict:
    return { 'id': int(m.group('id')), 'sets': [parse_set(set) for set in m.group('sets').split('; ')] } if (m := re.match( r'Game (?P<id>\d+): (?P<sets>.+)', game )) is not None else None

def parse(puzzle_input: str) -> list[dict]:
    """Parse input"""
    """
    return puzzle_input
    """
    return [parse_game(line) for line in puzzle_input.splitlines()]

def feasible_set(set: dict) -> bool:
    return  set['red']   <= 12 and \
            set['green'] <= 13 and \
            set['blue']  <= 14

def feasible_game(game: dict) -> bool:
    return all( [feasible_set(set) for set in game['sets']] )

def minimum_game(game: dict) -> list[int]:
    return [max( [set[color] for set in game['sets']] ) for color in ['red', 'green', 'blue']]

def power_of_game(game: dict) -> int:
    return math.prod( minimum_game(game) )

def part1(data):
    """Solve part 1"""
    return sum( [game['id'] for game in data if feasible_game(game)] )


def part2(data):
    """Solve part 2"""
    return sum( [power_of_game(game) for game in data] )


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
