import pathlib

import aoc_202303 as aoc
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
        ['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'],
        ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '3', '5', '.', '.', '6', '3', '3', '.'],
        ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
        ['6', '1', '7', '*', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '+', '.', '5', '8', '.'],
        ['.', '.', '5', '9', '2', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '7', '5', '5', '.'],
        ['.', '.', '.', '$', '.', '*', '.', '.', '.', '.'],
        ['.', '6', '6', '4', '.', '5', '9', '8', '.', '.'],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 4361


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == ...
