"""This module tests the find module in NamePy."""

import pytest
from src import find

def test_find_vars():
    """Check that assignment statement dictionary is outputted correctly."""
    path = "./test_files"
    assignment_dictionary = find.find_vars(path)
    correct_dictionary = {'__init__.py': 0, 'test_file.py': 6}
    assert assignment_dictionary == correct_dictionary

def test_var_length():
    """Check that the assignment statement tuple lengths are outputted correctly."""
    path = "./test_files"
    assignment_dictionary = find.var_length(path)
    correct_dictionary = None
    assert assignment_dictionary == correct_dictionary
