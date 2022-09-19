"""Docstring here."""
# from typing import List, Tuple, Dict, Optional
from typing import Dict
import libcst.matchers as match
import libcst as cst
# from src 
import generate_trees as generator

def generate_cast_single_file(path):
    """Generate a dictionary of a single file and its CAST.
    Args:
        path: The path of a file

    Returns:
        dict: Dictionary of file and corresponding CAST as value
    """
    string_file_dict = generator.read_single_file(path)
    cast_dict = generator.generate_cast(string_file_dict)

    return cast_dict

def generate_cast_directory(path):
    """Generate a dictionary of all of multiple files and CASTs.
    Args:
        path: The path of a directory

    Returns:
        dict: Dictionary of files in a directory and corresponding CASTs
    """
    file_list = generator.find_python_files(path)
    string_file_list = generator.read_files_in_directory(path, file_list)
    cast_dict = generator.generate_cast(string_file_list)

    return cast_dict

def file_or_directory(path):
    """Determine if path is for file or directory."""
    if path.endswith(".py"):
        cast_dict = generate_cast_single_file(path)
    else:
        cast_dict = generate_cast_directory(path)
    return cast_dict

def find_vars(path:str):
    var_dict = {}
    cast_dict = file_or_directory(path)
    for file, cast in cast_dict.items():
        var_list = match.findall(cast, match.Assign())
        # print(len(var_list))
        var_dict[file] = len(var_list)
    return var_dict

def var_length(path:str):
    cast_dict = file_or_directory(path)
    for cast in cast_dict.values():
        var_list = match.findall(cast, match.Assign())
        for var in var_list:
            targets = var.targets
            for var in targets:
                if isinstance(var.target, cst.Name):
                    print(len(var.target.value))
                else:
                    print("Error")

# (AssignTarget(target=Name(value='variable01',lpar=[],rpar=[],),whitespace_before_equal=SimpleWhitespace(value=' ',),whitespace_after_equal=SimpleWhitespace(value=' ',),),)\


# To find instances of variables, create dict of all variable names, create frequency table. Key is name of variable, value contains length of variable, how many times it was found, etc. Should do with object oriented.
# For instances where same variables are called in diff functions, do I care about individual functions, whole file...choose what i want ot measure.