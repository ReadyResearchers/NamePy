[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7538300&assignment_repo_type=AssignmentRepo)
# NamePy

# Thomas Antle

## Description of Prototype

Include an explanation of how the prototype fits into the larger project idea.

As I began designing my prototype and thinking about how I would implement it, I ran into blockers that I could not get past. The feasibility of my project idea quickly deteriorated, so I changed it. My new project idea is to create a tool and run experiments with it that deals with Python naming conventions. Namely, I am interesting in looking at the length of names (for instance, variable names) in comparison with the amount of times they are used in the source code. The premise of this idea stems from the fact that names in source code need to be descriptive. When a user is reviewing source code, a name that is used multiple times needs to be more descriptive than a name that may only be used once or twice. In this way, those that attempt to understand the source code have a better chance of understanding it. It is fairly unreasonable to make every name long and descriptive, but it is a good idea to make prevalent names as descriptive as possible. My prototype address this directly by finding names in Python source code and analyzing them based on preset standards (that will likely change with experimentation).

## Design

Include and describe the flowchart graphic in this section

![graphic](prototype-chart.jpg)

This flowchart connects all of the pieces that I planned out for my prototype. It starts at the terminal and connects things such as files, suites and environments together in an organized fashion.

## Features

There are two functioning features that lay some of the framework for the software tool. The first feature counts all assignments statements in the specified file(s). The second feature finds the length of each assignment statement tuple. As one would expect, the output for each statement is usually 1. For the feature in mind to be completed, the tuple needs to be separated by characters in order to find the length of the variables. Many other features will be implemented as the project continues.

## Installation requirements

The prototype is not yet set up with Poetry, so it is necessary to install the required libraries/dependencies locally. The latest version of Python should be installed. Installation instructions can be found [here](https://www.python.org/downloads/). In addition, LibCST and Typer are necessary for the prototype to run. They can be installed with the following commands.

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

## How to run prototype

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
