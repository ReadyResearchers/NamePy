# NamePy: An Identifier-Focused Linter for Novice Python Developers

### Thomas Antle

## Abstract

Programmatic identifiers are used by software developers to assign names to entities in their programs. They provide the foundation of program com- prehension and readability, so it is highly important that they are written clearly. Very few naming conventions exist that are required by programming languages, so developers and communities create clear names and standards on their own. Programmers develop this skill as they gain more experience, but the difficulty is high for those at a novice level. This research proposes NamePy, a Python tool that examines and evaluates identifiers in novice source code to help them learn this skill. It is designed to be implemented at the continuous integration level for ideal results. This research also includes an evaluation of the tool via an experimental study. The study uses open source Python files to evaluate the effectiveness of the tool’s ability to deter- mine experience levels. Conclusions are drawn based on NamePy’s results as compared to the expected results.

The full comprehensive article for NamePy can be found [here](https://github.com/Allegheny-ComputerScience-600-Sum2022/cmpsc-600-senior-thesis-antlet).

## Installation requirements

For local use, clone this repository. Once cloned, Poetry is used to install all of the required dependencies. The command to do so should be run in the NamePy directory:

```
poetry install
```

## Running NamePy

To run the tool, use the following command:

```
poetry run python namepy/visitor.py [FILE PATH]
```

# About

NamePy is designed to be used like other common linters (pylint, flake8, etc.). At either the local or continuous integration level, NamePy is run to produce errors, warning, and a rating out of 10.00. 

Checks:

- Assignment Variables
- Function Definitions
- Class Definitions
- Function Parameters

Checks for:

- Identifier Length
- Identifier Grammar
- Associated Comments/Docstrings

Errors relating to length and comments/docstrings are considered absolute with NamePy. Warnings related to grammar are considered suggestive. Because an NLP is used with no context for each identifier, it is not guaranteed that its part of speech tagging will always be accurate.