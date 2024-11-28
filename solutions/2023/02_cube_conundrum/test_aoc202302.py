import pathlib

import aoc_202302 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        { 'id': 1, 'sets': [ {'red': 4, 'green': 0, 'blue': 3}, {'red': 1, 'green': 2, 'blue': 6}, {'red': 0, 'green': 2, 'blue': 0} ] },
        { 'id': 2, 'sets': [ {'red': 0, 'green': 2, 'blue': 1}, {'red': 1, 'green': 3, 'blue': 4}, {'red': 0, 'green': 1, 'blue': 1} ] },
        { 'id': 3, 'sets': [ {'red': 20, 'green': 8, 'blue': 6}, {'red': 4, 'green': 13, 'blue': 5}, {'red': 1, 'green': 5, 'blue': 0} ] },
        { 'id': 4, 'sets': [ {'red': 3, 'green': 1, 'blue': 6}, {'red': 6, 'green': 3, 'blue': 0}, {'red': 14, 'green': 3, 'blue': 15} ] },
        { 'id': 5, 'sets': [ {'red': 6, 'green': 3, 'blue': 1}, {'red': 1, 'green': 2, 'blue': 2} ] }
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 8


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 2286


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == 68638
