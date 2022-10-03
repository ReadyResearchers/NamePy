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
def find_var_len(directory_path: str):
    """Find the length of each assignment statement tuple (temp)."""
    var_len_dict = find.var_length(directory_path)

@app.command()
def report(directory_path: str):
    """Find the length of each assignment statement tuple (temp)."""
    var_dict = find.find_vars(directory_path)
    print("\nNumber of variables per file:\n" + str(var_dict))
    print("\nVariable name legnths:")
    var_len_dict = find.var_length(directory_path)

if __name__ == "__main__":
    app()
