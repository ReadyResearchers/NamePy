# NamePy: An Identifier-Focused Linter for Novice Python Developers

### Thomas Antle

## Abstact

Programmatic identifiers are used by software developers to assign names to entities in their programs. They provide the foundation of program comprehension and readability, so it is highly important that they are written clearly. There are not many naming conventions that are required by programming languages, so developers and communities create clear names and standards on their own. Programmers develop this skill as they gain more experience, but the difficulty is high for students. NamePy a Python tool that examines and evaluates identifiers in students' source code to help them learn this skill. It is designed to be implemented at the continuous integration level for ideal results. This research also includes an evaluation of the tool via an experimental study. The study uses open source Python files to evaluate the effectiveness of the tool's ability to determine experience levels. Conclusions are drawn based on NapePy's results compared to the expected results.

An in-depth explanation of this concept can be found in my [Senior Thesis Proposal](SeniorThesisProposal.pdf).

### The following information is out of date and under construction:

## Installation requirements

For local use, clone this repository. Once cloned, Poetry is used to install all of the required dependencies. The command to do so should be run in the NamePy directory:

```
poetry install
```

## How to run tool

NamePy currently consists of 3 commands.

- `find-vars` - lists the number of assignment statements in the file specified or, if a directory is specified, lists the number of assignment statements in each file of the directory.
- `find-var-len` - lists the length of each assignment name in the order in which they appear in the file(s).
- `report` - runs both of the previous commands at once. This is a segway into reporting metrics in the future.

To run the tool, use the following command:

```
poetry run src/CLI.py [COMMAND] [PATH]
```

To run the suite of linters, use the following command:

```
poetry run task lint
```

To run the test suite, use the following command:

```
poetry run task test
```
