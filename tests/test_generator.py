"""This module tests the generate_trees module in NamePy."""

from src import generate_trees as generator

def test_find_python_files():
    """Test the ability of generator to find the python files in a directory."""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)
    number_of_files = len(file_list)

    assert number_of_files == 2


def test_find_test_file():
    """Test the ability of generator to find the test_file.py file in test_files."""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)

    assert "test_file.py" in file_list


def test_generate_cast():
    """Test if CASTs are being made correctly by LibCST."""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)
    string_file_dict = generator.read_files_in_directory(directory, file_list)

    cast_dict = generator.generate_cast(string_file_dict)

    assert len(cast_dict) == 2


def test_read_single_file():
    """Test input of a single file, rather than a directory."""
    file_path = "./test_files/test_file.py"
    cast_dict = generator.read_single_file(file_path)

    assert len(cast_dict) == 1
