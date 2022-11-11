"""Docstring here."""
import typer
# from src
from namepy import find

app = typer.Typer(
    name="namepy",
    help=("Description here.")
)

@app.command()
def find_vars(directory_path: str):
    """Find the amount of assignment statements in each file."""
    var_dict = find.find_vars(directory_path)
    print("Variables: " + str(var_dict))

@app.command()
def id_length(directory_path: str):
    """Report any errors or warnings related to identifier lengths."""
    find.variable_length(directory_path)
    find.function_length(directory_path)
    find.class_length(directory_path)
    find.parameter_length(directory_path)

@app.command()
def var_length(directory_path: str):
    """Report any errors or warnings related to identifier lengths."""
    find.variable_length(directory_path)

@app.command()
def report(directory_path: str):
    """x"""
    var_dict = find.find_vars(directory_path)
    func_dict = find.find_func_defs(directory_path)
    comment_dict = find.find_comments(directory_path)
    print("\nNumber of Identifiers per File:")
    print("\nVariables:\n" + str(var_dict))
    print("\nFunctions:\n" + str(func_dict))
    print("\nComments:\n" + str(comment_dict))
    print("")
    print("\nVariable name lengths:")
    var_len_dict = find.var_length(directory_path)

@app.command()
def find_func_defs(directory_path: str):
    """Find the function definitions in each file."""
    func_dict = find.find_func_defs(directory_path)
    print("Functions: " + str(func_dict))

@app.command()
def find_comments(directory_path: str):
    """Find the comments in each file."""
    comment_dict = find.find_comments(directory_path)
    print("Comments: " + str(comment_dict))

@app.command()
def find_classes():
    # directory_path: str
    """Find the comments in each file."""
    # class_dict = find.find_classes(directory_path)
    # print("Classes: " + str(class_dict))
    find_classes()

if __name__ == "__main__":
    app()


def func(param1,param2,param3):
    print("hello world")
    my_var = 1
    i = 9

def another_func(param1,param2,param3):
    print("hello world")
    my_var = 1
    # i is the number of watermelons
    i = 9


# We're only reading each file once, but when we reach certain nodes, we'll do a list of checks
# List of checks include: [Length checker, part of speech, comment checker on the line before]
# Implement a visitor
# Implement the visit_<node> function for each check we need
# Class names
# Function names
# Parameter Names
# variable names


# ?can you access a node parent from the node object?
