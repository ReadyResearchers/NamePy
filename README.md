# NamePy

# Thomas Antle

## The full proposal for NamePy can be found [here](SeniorThesisProposal.pdf)

## Features

There are two functioning features that lay some of the framework for the software tool. The first feature counts all assignments statements in the specified file(s). The second feature finds the length of each assignment statement tuple. *In progress

## Installation requirements

The tool is not yet set up with Poetry, so it is necessary to install the required libraries/dependencies locally. The latest version of Python should be installed. Installation instructions can be found [here](https://www.python.org/downloads/). In addition, LibCST and Typer are necessary for the prototype to run. They can be installed with the following commands.

```
pip install libcst
```

and

```
pip install typer
```

To test the prototype, Pytest is needed as well. It can be installed with the following command.

```
pip install pytest
```

## How to run tool

At the current stage, the prototype has two commands that can be run with the command line interface. The user should begin in the home directory. The template for the commands is shown below.

```
python src/CLI.py [COMMAND] [PATH]
```

The two available CLI commands are:

- `find-vars` - lists the number of assignment statements in the file specified or, if a directory is specified, lists the number of assignment statements in each file of the directory.
- `find-var-len` - outputs the number of tuple items are in each assignment statement (this is not the final, intended function of the feature, but it is where is currently stands).

To run the test suite the following command can be used.

```
pytest tests/
```

The test suite will not run the way the code is set up currently. The import statements need to be altered in order for either program to work or for the tests to work. To get them both working at the same time, I need to de-bug this issue.

## References

- https://www.python.org
- https://libcst.readthedocs.io/en/latest/
- https://typer.tiangolo.com

---
(Did you remember to add your name to the top of this document?)
