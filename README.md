# NamePy
## An Identifier-Focused Linter for Beginning Python Developers

# Thomas Antle

NamePy's purpose is to provide users with feedback that follows unique naming conventions. With this feedback, users will learn how to create effective Python identifiers and beneficial habits will be instilled. These effective identifiers will improve source code readability and comprehension.

An in-depth explanation of this concept at length can be found [here](SeniorThesisProposal.pdf).

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
