import pathlib

import aoc_202401 as aoc
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
    assert example1 == [[3, 4],[4, 3],[2, 5],[1, 3],[3, 9],[3,  3]]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 11


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 31


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == 24931009
