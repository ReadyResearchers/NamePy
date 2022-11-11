"""Docstring here."""
# from typing import List, Tuple, Dict, Optional
from typing import Dict
import libcst.matchers as match
import libcst as cst
# from src
from namepy import generate_trees as generator
# from spacy.lang.en import English
import sys


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

def variable_length(path:str):
    print("")
    print("Variable Names:")
    # print('\033[1m' + "\n\n** Running NAMEPY **")
    # print ('\033[0m')
    # while True:
    cast_dict = file_or_directory(path)
    for file, cast in cast_dict.items():
        # Returns a list of some objects
        # x,y = 10, 12
        var_list = match.findall(cast, match.Assign())
        for var in var_list:
            targets = var.targets
            for var in targets:
                with open(sys.argv[2]) as myFile:
                    for num, line in enumerate(myFile, 1):
                        # while True:
                            if isinstance(var.target, cst.Name):
                                # !lookup is assigned to first variable. If statement needs to reference
                                # !all variables. lookup needs to loop back and be reassigned
                                lookup = var.target.value
                                if lookup in line:
                                    # if isinstance(var.target, cst.Name):
                                        if (len(var.target.value)) <= 3:
                                            print ('Line', num, "in", [file], ":")
                                            print("  --ERROR--Variable '", (lookup), "' is of length", len(lookup), "-- Add a comment or increase length.")
                                        if (len(lookup)) >= 30:
                                            print ('Line', num, "in", [file], ":")
                                            print("  --WARNING--Variable '", (lookup), "' is of length", len(lookup), "-- Consider reducing length.")
                                        # !if num-1 has lookup, hashtag, and 2 other characters(space+1), pass
                                        # break

                            # if (len(var.target.value)) <= 3:
                            #     (print("  --ERROR--Variable '", (var.target.value), "' is of length", (len(var.target.value)), "-- Add a comment or increase length."))
                            # if (len(var.target.value)) >= 30:
                            #     print("  --WARNING--Variable '", (var.target.value), "' is of length", (len(var.target.value)), "-- Consider reducing length.")


def function_length(path:str):
    print("")
    print("Function Names:")
    cast_dict = file_or_directory(path)
    for file, cast in cast_dict.items():
        func_list = match.findall(cast, match.FunctionDef())
        # Find line number of given thing
        # lookup = 'x'
        # with open(sys.argv[2]) as myFile:
        #     for num, line in enumerate(myFile, 1):
        #         if lookup in line:
        #             print ('Line', num, "in", [file], ":")
        for func in func_list:
            if isinstance(func.name, cst.Name):
                # !If name is too short, require docstring
                if (len(func.name.value)) <= 3:
                    print("  --ERROR--Function Name '", (func.name.value), "' is of length", (len(func.name.value)), "-- Add a comment or increase length.")
                if (len(func.name.value)) >= 30:
                    print("  --WARNING--Function Name '", (func.name.value), "' is of length", (len(func.name.value)), "-- Consider reducing length.")


def class_length(path:str):
    print("")
    print("Class Names:")
    cast_dict = file_or_directory(path)
    for file, cast in cast_dict.items():
        class_list = match.findall(cast, match.ClassDef())
        # Find line number of given thing
        # lookup = 'x'
        # with open(sys.argv[2]) as myFile:
        #     for num, line in enumerate(myFile, 1):
        #         if lookup in line:
        #             print ('Line', num, "in", [file], ":")
        for classDef in class_list:
            if isinstance(classDef.name, cst.Name):
                if (len(classDef.name.value)) <= 3:
                    print("  --ERROR--Function Name '", (classDef.name.value), "' is of length", (len(classDef.name.value)), "-- Add a comment or increase length.")
                if (len(classDef.name.value)) >= 30:
                    print("  --WARNING--Function Name '", (classDef.name.value), "' is of length", (len(classDef.name.value)), "-- Consider reducing length.")


def parameter_length(path:str):
    print("")
    print("Parameter Names:")
    final_list = []
    necessary_nodes = []
    cast_dict = file_or_directory(path)
    for file, cast in cast_dict.items():
        func_list = match.findall(cast, match.FunctionDef())
    for func in func_list:
        # for i in func.params.params:
        # !need to look through all params, not just [0]
        if isinstance(func.params.params[0].name, cst.Name):
            # !check if name exists in docstring
            if (len(func.params.params[0].name.value)) <= 3:
                print("  --ERROR--Argument Name '", (func.params.params[0].name.value), "' is of length", (len(func.params.params[0].name.value)), "--Include in docstring or increase length.")
            if (len(func.params.params[0].name.value)) >= 30:
                print("  --WARNING--Argument Name '", (func.params.params[0].name.value), "' is of length", (len(func.params.params[0].name.value)), "--Consider reducing length.")


# comment_list = match.findall(cast, match.Comment())
# print("\nComments:")
# # for comment in comment_list:
#     # print(comment.value)

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

# print([file], ":")
# var_dict[var.target.value] = len(var.target.value)
# print(var_dict)
# print(len(var.target.value))