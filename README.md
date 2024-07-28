# Advent of Code

Solutions by Andrea Canidio

## Setup

Create a virtual environment:

```python -m venv .venv```

Activate the virtual environment:

```& .venv/Scripts/Activate.ps1```

Install the requirements:

```pip install -r requirements.txt```

## Solve a new code

Copy the template into a new solution folder

```cp -r .\template\ .\solutions\<year>\<day>_<name>```

where:

- ```year```: the quiz year
- ```day```: the quiz day in the year
- ```name```: the quiz name

Additionally, rename the ```aoc_template.py``` file to ```aoc_<year><day>.py```
and the test file ```test_aoc_template.py``` to ```test_aoc<year><day>.py```

Then change to the expected directory and finally download the examples files
from the Advent of Code website:

- ```example1```: the common example input inline with the quiz text
- ```example2```: the user-specific example input

To download the specific user-input run the following command:

```aocd <day> <year> > .\solutions\<year>\<day>_<name>\example2.txt```

### Manual solve

To solve a single example just execute the below command:

```python .\aoc_<year><day>.py .\example<id>.txt```

This is useful when developing the solution or to obtain a solution to load in
the website.

### Automatic solve (Pytest)

Check for solution correctness using the unit test:

```pytest```
