import pathlib
import sys

from enum import IntEnum

def to_values(list):
    """Convert sublist elements from letters to ordinal values"""
    adv_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
    }
    you_dict = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    return [[adv_dict[adv], you_dict[you]] for adv, you in list]


def parse(puzzle_input):
    """Parse input"""
    return to_values( [line.split(' ') for line in puzzle_input.split('\n')] )


def score_choice(x):
    """Returns the score given by your choice"""
    return x


def score_result(your_action, opponent_action):
    """Returns the score given by the match result"""
    victories = {
        1: [3],
        2: [1],
        3: [2]
    }

    defeats = victories[your_action]
    if your_action == opponent_action:
        return 3
    elif opponent_action in defeats:
        return 6
    return 0


def part1(data):
    """Solve part 1"""
    return sum([score_choice(you) + score_result(you, opp) for opp, you in data])


def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val][0]


def to_your_move(exp_result, opponent_action):
    """Returns your move based on the expected result and your opponent action"""
    victories = {
        1: 3,
        2: 1,
        3: 2
    }

    if exp_result == 2:
        return opponent_action
    elif exp_result == 1:
        return victories[opponent_action]
    return get_keys_from_value(victories, opponent_action)

def part2(data):
    """Solve part 2"""
    return sum([score_choice(to_your_move(exp_result, opp)) + score_result(to_your_move(exp_result, opp), opp) for opp, exp_result in data])


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
