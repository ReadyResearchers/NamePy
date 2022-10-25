"""Docstring here."""
# from typing import List, Tuple, Dict, Optional
from typing import Dict
import libcst.matchers as match
import libcst as cst
# from src
from namepy import generate_trees as generator
# from spacy.lang.en import English


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
        for var in var_list:
            targets = var.targets
            for var in targets:
                if isinstance(var.target, cst.Name):
                    var_dict[file] = len(var_list)
    return var_dict

def find_func_defs(path:str):
    func_dict = {}
    cast_dict = file_or_directory(path)
    for file, cast in cast_dict.items():
        func_list = match.findall(cast, match.FunctionDef())
        func_dict[file] = len(func_list)
    return func_dict

def find_comments(path:str):
    comment_dict = {}
    cast_dict = file_or_directory(path)
    for file, cast in cast_dict.items():
        comment_list = match.findall(cast, match.Comment())
        comment_dict[file] = len(comment_list)
    return comment_dict

# def find_classes():
    # path:str
    # class_dict = {}
    # cast_dict = file_or_directory(path)
    # for file, cast in cast_dict.items():
    #     class_list = match.findall(cast, match.ClassDef())
    #     class_dict[file] = len(class_list)
    # return class_dict
    # parser = English()
    # print(parser)

def identifier_length(path:str):
    print('\033[1m' + "\n\n** Running NAMEPY **")
    print ('\033[0m')
    # var_dict = {}
    cast_dict = file_or_directory(path)
    for file, cast in cast_dict.items():
    # for cast in cast_dict.values():
        var_list = match.findall(cast, match.Assign())
        func_list = match.findall(cast, match.FunctionDef())
        class_list = match.findall(cast, match.ClassDef())
        comment_list = match.findall(cast, match.Comment())
        # print("\nVariable Names:")
        print("\nIn", [file], ":")
        for var in var_list:
            targets = var.targets
            for var in targets:
                if isinstance(var.target, cst.Name):
                    # print([file], ":")
                    # var_dict[var.target.value] = len(var.target.value)
                    # print(var_dict)
                    # print(len(var.target.value))
                    if (len(var.target.value)) <= 3:
                    # if ((var.target.value) == "RUN" or (var.target.value) == "ast"):
                    # and has no comment:
                        # print([file], ":")
                        print("  --ERROR--Variable '", (var.target.value), "' is of length", (len(var.target.value)), "-- Add a comment or increase length.")
                        # print("--Variable '", (var.target.value), "' is of length", (len(var.target.value)), ". Watch our for obfuscation.")
                        # print((var.target.value))
                        # print(len(var.target.value))
                    if (len(var.target.value)) >= 30:
                        print("  --WARNING--Variable '", (var.target.value), "' is of length", (len(var.target.value)), "-- Consider reducing length.")

        # print("\nFunction Names:")
        # for func in func_list:
        #     if isinstance(func.name, cst.Name):
        #         if (len(func.name.value)) <= 10:
        #             print((func.name.value))
        #             print(len(func.name.value))
        #             print("too short")
        # print("\nClass Names:")
        # for classDef in class_list:
        #     if isinstance(classDef.name, cst.Name):
        #         if (len(classDef.name.value)) <= 30:
        #             print((classDef.name.value))
        #             print(len(classDef.name.value))
        #             print("too short")
        # print("\nComments:")
        # # for comment in comment_list:
        #     # print(comment.value)


# For length: if too short(3 or less), require a comment associated with it
# if comment is with short name, watch out for obfuscation
# if too long, suggest a smaller name


# Function to compare number of comments to number of identifiers
# def compare_comments():

# (AssignTarget(target=Name(value='variable01',lpar=[],rpar=[],),whitespace_before_equal=SimpleWhitespace(value=' ',),whitespace_after_equal=SimpleWhitespace(value=' ',),),)\

# To find instances of variables, create dict of all variable names, create frequency table. Key is name of variable, value contains length of variable, how many times it was found, etc. Should do with object oriented.
# For instances where same variables are called in diff functions, do I care about individual functions, whole file...choose what i want ot measure.

# Push dictionaries to big json file (or separate them to do categories)
# Controller makes dictionary with all function names 
# controller calls from FIND, pushes dicts to 
# for dict, look at primary keys and call them headers...etc.
# use viewer to look at dictionary, these keys are headers, these keys are blah
# look into reflection: if(callable)

# print(dir(namepy.find))

# from vars class, only run things that are this kind of function
# prefix all functions with _fxfind, _varfind, etc.
# can find all functions prefixed with __blank
# 